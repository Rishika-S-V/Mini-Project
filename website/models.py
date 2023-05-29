from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INTEGER, String, DATETIME, BOOLEAN
from sqlalchemy.sql import func


class Note(db.Model):
    id = Column(INTEGER, primary_key=True)
    data = Column(String(10000))
    date = Column(DATETIME(timezone=True), default=func.now())
    user_id = Column(INTEGER, ForeignKey("user.id"))


class Disaster(db.Model):
    id = Column(INTEGER, primary_key=True)
    title = Column(String(512))
    desc = Column(String(5000))
    location = Column(String(512))
    is_resolved = Column(BOOLEAN, default=False)
    user_id = Column(INTEGER, ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = Column(INTEGER, primary_key=True)
    email = Column(String(150), unique=True)
    password = Column(String(150))
    name = Column(String(150))
    notes = relationship("Note")
