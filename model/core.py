from sqlalchemy import Column, Integer, String, DateTime, Boolean

from .database import Base


class Process(Base):
    __tablename__ = 'captcha'

    id = Column(Integer, primary_key=True, index=True)
    captcha = Column()
    date = Column(DateTime)
    status = Column()

    answer = Column()

