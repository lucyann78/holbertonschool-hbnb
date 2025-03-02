from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        if not text:
            raise ValueError("Review text cannot be empty.")
        if not self.is_valid_user(user) or not self.is_valid_place(place):
            raise ValueError("Invalid user or place.")
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

        self.text = text
        self.rating = rating
        self.place = place  # Should be a Place instance
        self.user = user    # Should be a User instance

    @staticmethod
    def is_valid_user(user):
        # Lógica para validar si el user es válido
        return isinstance(user, User)  # Asegúrate de que sea una instancia de User

    @staticmethod
    def is_valid_place(place):
        # Lógica para validar si el place es válido
        return isinstance(place, Place)  # Asegúrate de que sea una instancia de Place
