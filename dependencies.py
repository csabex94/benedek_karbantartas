import jwt

from typing import Annotated
from fastapi import Cookie, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from jwt.exceptions import InvalidTokenError
from utils.exception_handler import CustomExceptionHandler

from utils.config import get_settings, Settings
from database.db_session import get_db_session
from models import User

app_settings: Settings = get_settings()

def get_current_user(access_token: Annotated[str | None, Cookie()] = None):
    try:
        payload = jwt.decode(access_token, app_settings.jwt_secret, algorithms=[app_settings.jwt_algorithm])
        return payload
    except InvalidTokenError:
        raise CustomExceptionHandler('unauthorized', 'Access Denied', 401)

DB_SESSION = Annotated[AsyncSession, Depends(get_db_session)]
    
CURRENT_USER = Annotated[User | None, Depends(get_current_user)]