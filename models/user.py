from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Binary
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from . import base

Base = base.Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String)
    pw_hashed = Column(Binary)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_admin = Column(Boolean)

    activity = relationship("Activity", backref="users")

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
