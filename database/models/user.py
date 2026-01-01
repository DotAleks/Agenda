from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger

from .base import Base



class User(Base):
    __tablename__ = 'users'
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str] = mapped_column()

