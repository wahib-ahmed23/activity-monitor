from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime


class Base(DeclarativeBase):
    pass


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True, index=True)

    process = Column(String)

    window_title = Column(String)

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    duration = Column(Integer)