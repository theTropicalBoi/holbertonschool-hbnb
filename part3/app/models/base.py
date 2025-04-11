from app.extensions import db
import uuid
from datetime import datetime
from typing import List


class BaseModel(db.Model): 
    __abstract__ = True
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()
        db.session.commit()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save() 
        
    def to_dict(self, excluded_attr: List[str] = []):
        """Convert the object attributes to a dictionary, excluding specified attributes."""
        result = {}
        for key, value in self.__dict__.items():
            if key.startswith('_') or key in excluded_attr or isinstance(value, datetime):
                continue
            if isinstance(value, BaseModel):
                result[key] = value.to_dict(excluded_attr)
            else:
                result[key] = value
        return result
        
        