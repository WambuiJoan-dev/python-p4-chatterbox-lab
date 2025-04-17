from faker import Faker
from models import db, Message  # Updated import statement
from app import app  # Import the app for context

fake = Faker()

def seed_messages(n=10):
    for _ in range(n):
        message = Message(
            body=fake.text(),
            username=fake.user_name()
        )
        db.session.add(message)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():  # Set up application context
        db.create_all()  # Create tables
        seed_messages()  # Seed the database
