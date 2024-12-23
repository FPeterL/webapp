from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("aA123456")
print(hashed_password)
