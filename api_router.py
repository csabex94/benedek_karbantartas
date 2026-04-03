
from typing import List
from fastapi import APIRouter

from fastapi.responses import JSONResponse
from utils.config import get_settings, Settings
from models import CreateUser, LoginUser, User
from services.authentication import create_user, login_user, get_all_users
from dependencies import DB_SESSION, CURRENT_USER

app_settings: Settings = get_settings()

api_router = APIRouter(prefix="/api/v1")
    
@api_router.post("/create-user", response_model=User)
async def create_new_user(createUser: CreateUser, db: DB_SESSION):
    user = await create_user(db=db, createUser=createUser)
    return user

@api_router.post("/login", response_model=User)
async def login(loginUser: LoginUser, db: DB_SESSION):
    [token, user] = await login_user(db=db, loginUser=loginUser)
    response = JSONResponse(content=user)
    response.set_cookie(key="access_token", value=token, httponly=True, secure=False)
    return response

@api_router.get("/get-users", response_model=List[User])
async def get_users(db: DB_SESSION):
    result = await get_all_users(db)
    return result

@api_router.get("/me", response_model=User)
async def me(user: CURRENT_USER):
    return user