from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str
    api_key_secret: str
    jwt_secret: str
    jwt_algorithm: str
    jwt_token_expire_minutes: str
    mail_smtp_server: str
    mail_smtp_port: int
    mail_smtp_user: str
    mail_smtp_password: str
    mail_smtp_tls: bool
    mail_smtp_ssl: bool
    mail_smtp_from: str
    mail_smtp_use_credentials: bool


    class Config:
        env_file: str = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()

@lru_cache()
def get_settings()-> Settings:
    return settings