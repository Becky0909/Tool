"""
开发环境配置
"""
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: Optional[str] = "/ReDoc"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'root'
    MYSQL_PASSWORD: str = "123456"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    # MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "218.17.39.34"
    MYSQL_DATABASE: str = 'Tools'

    # Mysql地址
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:19990909@127.0.0.1:3306/test?charset=utf8"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"


config = Config()
