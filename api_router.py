
from typing import Annotated, List
from fastapi import APIRouter, Cookie, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi.responses import JSONResponse
from utils.config import get_settings, Settings
from database.db_session import get_db_session
from models import CreateUser, LoginUser, User
from services.authentication import create_user, login_user, get_all_users, get_current_user

app_settings: Settings = get_settings()

api_router = APIRouter(prefix="/api/v1")

db_session = Annotated[AsyncSession, Depends(get_db_session)]
    
async def get_me(access_token: Annotated[str | None, Cookie()] = None):
    response = await get_current_user(token=access_token, secret=app_settings.jwt_secret, algorithm=app_settings.jwt_algorithm)
    return response

get_current_user_dependencie = Annotated[User | None, Depends(get_me)]
    
@api_router.post("/create-user", response_model=User)
async def create_new_user(createUser: CreateUser, db: db_session):
    user = await create_user(db=db, createUser=createUser)
    return user

@api_router.post("/login", response_model=User)
async def login(loginUser: LoginUser, db: db_session):
    [token, user] = await login_user(db=db, loginUser=loginUser, secret=app_settings.jwt_secret, algorithm=app_settings.jwt_algorithm)
    response = JSONResponse(content=User(**user.model_dump()).model_dump())
    response.set_cookie(key="access_token", value=token, httponly=True, secure=False)
    return response

@api_router.get("/get-users", response_model=List[User])
async def get_users(db: db_session):
    result = await get_all_users(db)
    return result

@api_router.get("/me", response_model=User)
async def me(user: get_current_user_dependencie):
    return user