from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from . import base
Base = base.Base


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    description = Column(String)
    assoc_user = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Activity(User='%s', Description='%s')>" % (self.assoc_user, self.description)
