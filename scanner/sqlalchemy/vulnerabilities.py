from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from scanner import Base


class Vulnerabilities(Base):
    __tablename__ = 'vulnerabilities'

    # table attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    severity_level = Column(Integer)  # in range from 1 to 10
    endpoint = Column(String)
    description = Column(String)
