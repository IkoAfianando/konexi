from flask import jsonify, request
from flask_jwt_extended import create_access_token, JWTManager
from app.repositories.user_repository import UserRepository
import bcrypt
from app import jwt

def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return jsonify({'message': 'Username and password are required'}), 400

    new_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user_repo = UserRepository()
    existing_user = user_repo.get_by_username(username)
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    new_user = user_repo.create(username, new_password)
    return jsonify({'message': 'User created successfully'}), 201


def login():

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_repo = UserRepository()
    user = user_repo.get_by_username(username)

    if not user:
        return jsonify({'message': 'User Not Found'}), 404

    is_valid_password = bcrypt.checkpw(password.encode('utf-8'), user['password'])

    if is_valid_password is False:
        return jsonify({'message': 'Wrong Password'}), 400

    access_token = create_access_token(identity=str(user['_id']))
    return jsonify({'access_token': access_token}), 200
