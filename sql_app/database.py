from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setting import config

# SQL alchemy引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
# sessionmaker 会话生成器
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
