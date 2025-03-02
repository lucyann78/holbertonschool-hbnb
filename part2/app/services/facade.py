from app.models.user import User
from app.models.amenity import Amenity  # Ensure you import Amenity
from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()  # Add amenity repository

    # User-related methods
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    # Amenity-related methods
    def create_amenity(self, amenity_data):
        new_amenity = Amenity(**amenity_data)
        self.amenity_repo.add(new_amenity)  # Save new amenity to the repository
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return list(self.amenity_repo.users.values())  # Assuming amenities are stored as users

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            amenity.name = amenity_data.get('name', amenity.name)
            # Save changes to the repository (if needed)
            return amenity
        return None

# InMemoryRepository could be a subclass of UserRepository that implements in-memory storage
class UserRepository:
    def add_user(self, user):
        # Logic to add user to the database
        pass

    def get_user_by_id(self, user_id):
        # Logic to get user by ID
        pass

class InMemoryRepository(UserRepository):
    def __init__(self):
        self.users = {}  # Dictionary to hold users in memory
        self.next_id = 1  # Simple ID counter

    def add(self, user):
        user.id = self.next_id  # Assign an ID to the user
        self.users[self.next_id] = user
        self.next_id += 1

    def get(self, user_id):
        return self.users.get(user_id)

    def get_by_attribute(self, attribute, value):
        for user in self.users.values():
            if getattr(user, attribute, None) == value:
                return user
        return None
    class HBnBFacade:
    def create_place(self, place_data):
        # Validate and create a new place
        # Example validation
        place = Place(**place_data)
        # Add to database session and commit
        pass

    def get_place(self, place_id):
        # Retrieve a place by ID
        # Include associated owner and amenities
        pass

    def get_all_places(self):
        # Retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Update a place with new data
        pass
    from sqlalchemy.orm import Session
from app.models.review import Review
from app.models.user import User  # Assuming User model exists
from app.models.place import Place  # Assuming Place model exists

class HBnBFacade:
    def __init__(self, session: Session):
        self.session = session

    def create_review(self, review_data):
        user = self.session.query(User).filter_by(id=review_data['user_id']).first()
        place = self.session.query(Place).filter_by(id=review_data['place_id']).first()
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")
        
        review = Review(
            id=generate_unique_id(),  # Implement a function to generate unique IDs
            text=review_data['text'],
            rating=review_data['rating'],
            user_id=review_data['user_id'],
            place_id=review_data['place_id']
        )
        self.session.add(review)
        self.session.commit()
        return review

    def get_review(self, review_id):
        review = self.session.query(Review).filter_by(id=review_id).first()
        if not review:
            raise ValueError("Review not found")
        return review

    def get_all_reviews(self):
        return self.session.query(Review).all()

    def get_reviews_by_place(self, place_id):
        return self.session.query(Review).filter_by(place_id=place_id).all()

    def update_review(self, review_id, review_data):
        review = self.session.query(Review).filter_by(id=review_id).first()
        if not review:
            raise ValueError("Review not found")
        
        review.text = review_data.get('text', review.text)
        review.rating = review_data.get('rating', review.rating)
        self.session.commit()
        return review

    def delete_review(self, review_id):
        review = self.session.query(Review).filter_by(id=review_id).first()
        if not review:
            raise ValueError("Review not found")
        
        self.session.delete(review)
        self.session.commit()
