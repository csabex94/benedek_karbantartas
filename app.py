from fastapi import FastAPI, Request, Response
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from database.schemas import migrate
from database.db_session import sessionmanager
from api_router import api_router
from utils.exception_handler import CustomExceptionHandler
from utils.security_utils import generate_request_id

@asynccontextmanager
async def lifespan():
    await migrate(sessionmanager._engine)
    yield
    if sessionmanager._engine is not None:
        await sessionmanager.close()
    

origins = ["http://localhost:5173"]

app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(CustomExceptionHandler)
async def custom_exception_handler(request: Request, exception: CustomExceptionHandler):
    return JSONResponse(status_code=exception.status_code, content=exception.content)

@app.middleware("http")
async def add_security_headers(request, call_next):
    response: Response = await call_next(request)
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.set_cookie(key='request_id', value=generate_request_id())
    return response