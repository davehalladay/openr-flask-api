from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Activity(Base):
    __tablename__ = "activity"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    description = Column(String)
    assoc_user = Column(Integer, ForeignKey('user.id'))

    user = relationship("User", back_populates="activity")

    def __repr__(self):
        return "<Activity(User='%s', Description='%s')>" % (self.assoc_user, self.description)
