from __future__ import annotations
from database.db import db
from models.model import Model, datetime

class UserModel(db.Model, Model):
    __tablename__ = 'users'

    id         = db.Column(db.Integer, primary_key = True)
    username   = db.Column(db.String(100), nullable = False, unique = True)
    password   = db.Column(db.String(250), nullable = False)
    created_at = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    updated_at = db.Column(db.Date())

    def __init__(self, _id: int, username: str, password: str, created_at: datetime = None, updated_at: datetime = None) -> None:
        self.id         = _id
        self.username   = username
        self.password   = password
        self.created_at = created_at
        self.updated_at = updated_at
    
    def json(self) -> dict:
        return {
            'username': self.username,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def find_by_username(cls, username: str) -> Model:
        return cls.query.filter_by(username = username).first()