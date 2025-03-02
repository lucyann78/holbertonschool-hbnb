from app.models.user import User
from app.models.amenity import Amenity  # Asegúrate de importar Amenity
from app.persistence.repository import InMemoryRepository
from sqlalchemy.orm import Session
from app.models.review import Review
from app.models.place import Place  # Asumiendo que el modelo Place existe

class HBnBFacade:
    def __init__(self, session: Session):  # Agrega el parámetro session
        self.session = session  # Almacena el session
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository() 

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
        self.amenity_repo.add(new_amenity)  # Guarda la nueva amenidad en el repositorio
        return new_amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return list(self.amenity_repo.amenities.values())  # Asegúrate de que amenities esté definido

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            amenity.name = amenity_data.get('name', amenity.name)
            return amenity
        return None

    # Place-related methods
    def create_place(self, place_data):
        # Validar y crear un nuevo lugar
        place = Place(**place_data)
        self.session.add(place)  # Agregar a la sesión de la base de datos
        self.session.commit()
        return place

    def get_place(self, place_id):
        return self.session.query(Place).filter_by(id=place_id).first()  # Recuperar un lugar por ID

    def get_all_places(self):
        return self.session.query(Place).all()  # Recuperar todos los lugares

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if place:
            for key, value in place_data.items():
                setattr(place, key, value)
            self.session.commit()
            return place
        return None

    # Review-related methods
    def create_review(self, review_data):
        user = self.session.query(User).filter_by(id=review_data['user_id']).first()
        place = self.session.query(Place).filter_by(id=review_data['place_id']).first()
        if not user or not place:
            raise ValueError("Invalid user_id or place_id")

        review = Review(
            id=generate_unique_id(),  # Implementa una función para generar IDs únicos
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

# InMemoryRepository podría ser una subclase de UserRepository que implementa almacenamiento en memoria
class UserRepository:
    def add_user(self, user):
        # Lógica para agregar usuario a la base de datos
        pass

    def get_user_by_id(self, user_id):
        # Lógica para obtener usuario por ID
        pass

class InMemoryRepository(UserRepository):
    def __init__(self):
        self.users = {}  # Diccionario para mantener usuarios en memoria
        self.amenities = {}  # Diccionario para mantener amenidades en memoria
        self.next_id = 1  # Contador simple de IDs

    def add(self, item):
        item.id = self.next_id  # Asigna un ID al ítem
        if isinstance(item, User):
            self.users[self.next_id] = item
        elif isinstance(item, Amenity):
            self.amenities[self.next_id] = item
        self.next_id += 1

    def get(self, item_id):
        return self.users.get(item_id) or self.amenities.get(item_id)

    def get_by_attribute(self, attribute, value):
        for user in self.users.values():
            if getattr(user, attribute, None) == value:
                return user
        return None
