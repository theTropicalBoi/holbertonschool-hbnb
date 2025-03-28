from .basemodel import BaseModel
from app.extensions import db



class Amenity(BaseModel):
	__tablename__ = 'amenities'
	

	name = db.Column(db.String(), nullable=False)

	# @Daniel TODO - Add Table Relationship: Places 
	places = db.relationship('Place', backref='amenity')

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		if not isinstance(value, str):
			raise TypeError("Name must be a string")
		if not value:
			raise ValueError("Name cannot be empty")
		super().is_max_length('Name', value, 50)
		self.__name = value

	def update(self, data):
		return super().update(data)
	
	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name
		}
