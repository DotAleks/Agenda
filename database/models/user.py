from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger

from typing import List

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    tasks: Mapped[List["Task"]] = relationship(
        "Task", 
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
