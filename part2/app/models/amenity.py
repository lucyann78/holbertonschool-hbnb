from .base_model import BaseModel
import uuid

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the amenity
        self.name = name
        self.validate()

    def validate(self):
        if not self.name or len(self.name) > 50:
            raise ValueError("Amenity name must be provided and under 50 characters.")
