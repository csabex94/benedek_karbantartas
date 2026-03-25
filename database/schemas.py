import uuid
from typing import Optional
from sqlalchemy import Column
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.asyncio import AsyncEngine
from datetime import datetime

class UserSchema(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    email: Optional[str] = Field(default=None, nullable=False)
    fullname: Optional[str] = Field(default=None, nullable=False)
    password: Optional[str] = Field(default=None, nullable=False, min_length=8)
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now())


class StoreSchema(SQLModel, table=True):
    __tablename__ = "stores"
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    name: Optional[str] = Field(default=None, nullable=False)
    city: Optional[str] = Field(default=None, nullable=False)
    country: Optional[str] = Field(default=None, nullable=False)
    ip_address: Optional[str] = Field(default=None, nullable=False)


async def migrate(engine: AsyncEngine):
    async with engine.connect() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)