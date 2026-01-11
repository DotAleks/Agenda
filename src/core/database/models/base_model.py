from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs


class BaseModel(AsyncAttrs, DeclarativeBase):
    """The base class for all SQLAlchemy models with async support.

    Automatically generates table names in snake_case based on class names and adds the standard 'id' field as a primary key.
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Automatically generates a table name based on the class name.

        Converts CamelCase to snake_case and appends an 's' to the end:
        - User → users
        - OrderItem → order_items
        """
        import re

        name = cls.__name__
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        snake_case_name = re.sub("([a-z0-9])([A_Z])", r"\1_\2", s1).lower()
        return snake_case_name + "s"

    id: Mapped[int] = mapped_column(primary_key=True)
