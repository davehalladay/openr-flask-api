from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    pw_hashed = Column(String)
    salt = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)
