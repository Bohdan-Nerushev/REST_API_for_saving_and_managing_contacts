from faker import Faker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src import models, database  # Змінюйте ці імпорти відповідно до вашої структури

fake = Faker()

def create_fake_contact():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "birthday": fake.date_of_birth(minimum_age=18, maximum_age=90),  # Переконайтеся, що це об'єкт типу date
        "additional_info": fake.text(max_nb_chars=200)
    }

def populate_database(num_contacts: int):
    # Ініціалізуйте підключення до бази даних
    engine = create_engine(database.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Створіть нову сесію
    with SessionLocal() as db:
        # Створіть контакти
        contacts = [models.Contact(**create_fake_contact()) for _ in range(num_contacts)]
        
        # Додайте контакти до сесії
        db.add_all(contacts)
        db.commit()

if __name__ == "__main__":
    populate_database(200)

