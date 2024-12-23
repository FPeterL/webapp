from werkzeug.security import generate_password_hash
from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin@localhost:27017/")
db = client.get_database()
users = db.users

# Új felhasználó hozzáadása a MongoDB-be
password_hash = generate_password_hash("password123")  # Titkosítja a jelszót
users.insert_one({"username": "admin", "password": password_hash})