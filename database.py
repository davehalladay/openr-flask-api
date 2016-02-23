import os
import time

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
import bcrypt

from models.base import Base
from models.activity import Activity
from models.user import User


database = {
    'drivername': 'postgres',
    'host': os.environ['DB_HOST'],
    'port': os.environ['DB_PORT'],
    'username': os.environ['DB_USER'],
    'password': os.environ['DB_PW'],
    'database': os.environ['DB_NAME']
}
engine = create_engine(URL(**database))
Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)


def create_user(name, password, **kwargs):
    session = Session()
    data = {
        "name": name,
        "email": kwargs.get("email"),
        "pw_hashed": bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()),
        "is_admin": kwargs.get("is_admin")
    }
    new_user = User(**data)
    session.add(new_user)
    session.commit()
    return new_user.id


def log_activity(user_id, activity_desc):
    session = Session()
    activity = Activity(assoc_user=user_id, description=activity_desc, created_at=time.time())
    session.add(activity)
    session.commit()
    return True
