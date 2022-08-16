from typing_extensions import Required
from flask_sqlalchemy import SQLAlchemy
from pkg_resources import require
from traitlets import default

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """adopt."""

    __tablename__ = "adopt"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True ) 
    name = db.Column(db.Text, nullable=False)
    species= db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text,nullable=True)
    age=db.Column(db.Integer,nullable=True)
    notes=db.Column(db.Text,nullable=True)
    available= db.Column(db.Boolean, nullable=False, default=True )