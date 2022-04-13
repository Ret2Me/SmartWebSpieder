from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from scanner import Base


class Servers(Base):
    __tablename__ = 'servers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    timestamp = Column(DateTime)
    vulnerability_id = Column(Integer, ForeignKey('vulnerabilities.id'))
    confidence = Column(Integer)
    vulnerability = relationship("Vulnerabilities")

    def serialize(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

