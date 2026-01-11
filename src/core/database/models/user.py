from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class User(BaseModel):
    """The user entity in the system.

    Attributes:
        tg_id: Telegram User ID
    """

    tg_id: Mapped[int] = mapped_column(unique=True, index=True)
    tasks: Mapped[list["tasks"]] = relationship(  # type: ignore
        back_populates="user", cascade="all, delete-orphan"
    )
