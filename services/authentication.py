import jwt

from datetime import datetime, timedelta, timezone
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from database.schemas import UserSchema
from models import CreateUser, LoginUser, User
from utils.security_utils import password_hash, password_check
from utils.exception_handler import CustomExceptionHandler
from utils.config import get_settings, Settings

app_settings: Settings = get_settings()

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app_settings.jwt_secret, algorithm=app_settings.jwt_algorithm)
    return encoded_jwt

async def get_user_by_email(db: AsyncSession, email: str) -> UserSchema | None:
    stmt = select(UserSchema).where(UserSchema.email == email)
    result = await db.scalars(stmt)
    user: UserSchema | None = result.first()
    return user

async def get_all_users(db: AsyncSession):
    stmt = select(UserSchema)
    result = await db.scalars(stmt)
    users = result.all()
    return users

async def create_user(db: AsyncSession, createUser: CreateUser):
    user = await get_user_by_email(db, createUser.email)
    
    if user is not None:
        raise CustomExceptionHandler('resource_already_exists', 'User already exists', 409)
    
    userSchema = UserSchema(
        email=createUser.email,
        fullname=createUser.fullname,
        password=password_hash(createUser.password)
    )
    
    db.add(userSchema)
    await db.commit()
    await db.refresh(userSchema)
    return userSchema


async def login_user(db: AsyncSession, loginUser: LoginUser):
    user = await get_user_by_email(db, loginUser.email)
    
    if user is None:
        raise CustomExceptionHandler('not_found', 'User not found or not exists', 404)
    
    attempt = password_check(loginUser.password, user.password)
    
    if attempt is False:
        raise CustomExceptionHandler('incorrect_password', 'Incorrect password', 422)
    data={"id": user.id, "fullname": user.fullname, "email": user.email}
    access_token = create_access_token(data=data)
    return [access_token, data]
