from cgi import parse_multipart
from enum import Enum
from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from database import Base
from pydantic import BaseModel


class CounterTable(Base):
    __tablename__ = "counts"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, primary_key=False, index=False)

class IncrementalChange(Enum):
    add = 1
    substract = -1


class CountChangeRequest(BaseModel):
    change: IncrementalChange

class Addition(BaseModel):
    change = 1

class Substraction(BaseModel):
    change = -1