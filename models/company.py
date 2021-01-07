from database.db import db
from models.model import Model, datetime, string_to_date
from models.product import ProductModel
from models.presentation import PresentationModel

class CompanyModel(db.Model, Model):
    __tablename__ = 'companies'

    id            = db.Column(db.Integer, primary_key = True)
    name          = db.Column(db.String(100), nullable = False, unique = True)
    position      = db.Column(db.String(100), nullable = False)
    assignments   = db.Column(db.String(1000))
    started_at    = db.Column(db.Date(), nullable = False, default = datetime.date.today())
    ended_at      = db.Column(db.Date())
    segment_id    = db.Column(db.Integer, db.ForeignKey('segments.id'), nullable = False, default = 1)
    segment       = db.relationship('SegmentModel')
    products      = db.relationship('ProductModel', lazy='dynamic')
    presentations = db.relationship('PresentationModel', lazy='dynamic')

    def __init__(self, name, position, assignments, started_at, segment_id, ended_at = None, _id = None):
        self.id          = _id
        self.name        = name
        self.position    = position
        self.assignments = assignments
        self.started_at  = string_to_date(started_at)
        self.ended_at    = string_to_date(ended_at) if ended_at else None
        self.segment_id  = segment_id

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'assignments': self.assignments,
            'started_at': self.started_at.isoformat(),
            'ended_at': self.ended_at.isoformat() if self.ended_at else None,
            'segment': {'id': self.segment.id, 'name': self.segment.name},
            'products': [product.json() for product in self.products.all()],
            'presentations': [presentation.json() for presentation in self.presentations.all()]
        }
    
    def curriculum_json(self):
        return {
            'id': self.id, 
            'name': self.name, 
            'position': self.position, 
            'started_at': self.started_at.isoformat(),
            'ended_at': self.ended_at.isoformat() if self.ended_at else None
        }