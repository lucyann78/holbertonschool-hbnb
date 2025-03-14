from .base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()  # Llama al constructor de BaseModel
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.validate()  # Llama al método de validación

    def validate(self):
        if len(self.first_name) > 50 or len(self.last_name) > 50:
            raise ValueError("First and last names must be under 50 characters.")
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format.")

    @staticmethod
    def is_valid_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None
