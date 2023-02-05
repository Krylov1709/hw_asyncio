from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


PG_DSN = 'postgresql+asyncpg://postgres:Rhskjd@localhost:5432/asyncio_db'
engine = create_async_engine(PG_DSN)
Base = declarative_base()


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String,)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(JSON)
    films = Column(JSON)
    species = Column(JSON)
    vehicles = Column(JSON)
    starships = Column(JSON)
    created = Column(String)
    edited = Column(String)
    url = Column(String)


Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

