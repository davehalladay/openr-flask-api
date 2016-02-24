import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
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
session = Session()


def create_user(name, password, **kwargs):
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


def update_user(id, **kwargs):
    try:
        user = session.query(User).filter(User.id == id).one()
    except (MultipleResultsFound, NoResultFound):
        return False
    if kwargs["name"]:
        user.name = kwargs["name"]
    if kwargs["email"]:
        user.email = kwargs["email"]
    if kwargs["is_admin"] is not None:
        user.is_admin = kwargs["is_admin"]
    if kwargs["password"]:
        user.pw_hashed = bcrypt.hashpw(kwargs["password"].encode("utf-8"), bcrypt.gensalt())
    session.add(user)
    session.commit()
    return True


def get_user(id):
    try:
        user = session.query(User).filter(User.id == id).one()
    except (MultipleResultsFound, NoResultFound):
        return None
    return user


def delete_user(id):
    user = session.query(User).filter(User.id == id).one()
    session.delete(user)
    session.commit()
    return True


def log_activity(user_id, activity_desc):
    session = Session()
    activity = Activity(assoc_user=user_id, description=activity_desc)
    session.add(activity)
    session.commit()
    return True
