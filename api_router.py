from fastapi import APIRouter

from utils.config import get_settings, Settings

app_settings: Settings = get_settings()

api_router = APIRouter(prefix="/api/v1")

@api_router.get('/test')
async def test():
    return {
        "ok": True,
        "settings": app_settings
    }