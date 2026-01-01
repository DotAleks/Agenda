from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass
class Config:
    BOT_TOKEN: str

    DB_DRIVER: str
    DB_USER: str
    DB_PASSWD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def DB_URL(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    @classmethod
    def from_env(cls, env: str = '.env'):
        load_dotenv(env)
        bot_token = cls._get_required('BOT_TOKEN')

        db_driver = cls._get_required('DB_DRIVER')
        db_user = cls._get_required('DB_USER')
        db_passwd = cls._get_required('DB_PASSWD')
        db_host = cls._get_optional('DB_HOST','localhost')
        db_port = int(cls._get_required('DB_PORT'))
        db_name = cls._get_required('DB_NAME')
        return cls(
            BOT_TOKEN=bot_token,
            DB_DRIVER=db_driver,
            DB_USER=db_user,
            DB_PASSWD=db_passwd,
            DB_HOST=db_host,
            DB_PORT=db_port,
            DB_NAME=db_name)
    
    @staticmethod
    def _get_required(key: str):
        value = os.getenv(key)
        if not value or not value.strip():
            raise ValueError(f'Required environment variable "{key}" is not set or empty')
        return value
    
    @staticmethod
    def _get_optional(key: str, default_value):
        return os.getenv(key,default_value)
    
config = Config.from_env()
