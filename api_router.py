from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

@api_router.get('/test')
async def test():
    return {
        "ok": True
    }