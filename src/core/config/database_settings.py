from pydantic_settings import BaseSettings
from pydantic import Field
from urllib.parse import quote_plus


class DatabaseSettings(BaseSettings):
    """"""

    driver: str = Field("postgresql+asyncpg", alias="DB_DRIVER")
    host: str = Field("localhost", alias="DB_HOST")
    port: int = Field(5432, alias="DB_PORT")
    user: str = Field("", alias="DB_USER")
    password: str = Field("", alias="DB_PASSWD")
    database: str = Field("", alias="DB_NAME")
    echo: bool = Field(False, alias="DB_ECHO")

    @property
    def url(self) -> str:
        password = quote_plus(self.password)

        return f"{self.driver}://{self.user}:{password}@{self.host}:{self.port}/{self.database}"
