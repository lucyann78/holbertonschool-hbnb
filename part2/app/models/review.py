from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place  # Should be a Place instance
        self.user = user  # Should be a User instance
        self.validate()

    def validate(self):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
