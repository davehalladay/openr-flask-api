from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    description = Column(String)
    assoc_user = Column(Integer)

    def __repr__(self):
        return "<Activity(User='%s')>" % self.assoc_user
