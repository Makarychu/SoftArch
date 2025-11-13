from jose import jwt

SECRET_KEY = "super_secret_key"
ALGORITHM = "HS256"

data = {"user_id": 1, "username": "admin"}
token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
print(token)
