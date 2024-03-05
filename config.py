from json import loads, dumps
from typing import Optional

import dotenv
from pydantic.networks import PostgresDsn, HttpUrl
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Config(BaseSettings):
    aws_access_key_id:str
    aws_secret_access_key:str
    aws_bucket_name:str

    class Config:
        env_prefix = "test_"


config = Config()
