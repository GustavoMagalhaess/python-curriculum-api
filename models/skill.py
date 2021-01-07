from database.db import db
from models.model import Model, datetime

class SkillModel(db.Model, Model):
    __tablename__ = 'skills'

    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.String(1000), nullable = False)
    level       = db.Column(db.Integer, nullable = False)
    created_at  = db.Column(db.Date(), nullable = False, default = datetime.date.today(), unique = True)
    segment_id  = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment     = db.relationship('SegmentModel')

    def __init__(self, name, description, level, segment_id, _id = None):
        self.id          = _id
        self.name        = name
        self.description = description
        self.level       = level
        self.segment_id  = segment_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'level': self.level,
            'created_at': self.created_at.isoformat(),
            'segment': {'id': self.segment.id, 'name': self.segment.name}
        }
    
    def curriculum_json(self):
        return {'id': self.id, 'name': self.name, 'level': self.level}