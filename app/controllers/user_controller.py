from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.repositories.user_repository import UserRepository
import bcrypt


@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user_repo = UserRepository()
    user = user_repo.get_by_id(user_id)
    return jsonify({'username': user['username']}), 200

@jwt_required()
def update_user():
    data = request.get_json()
    password = data.get('password')

    user_id = get_jwt_identity()
    user_repo = UserRepository()
    user = user_repo.get_by_id(user_id)

    new_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    update_password = user_repo.update_password(user_id, new_password)

    return jsonify({'message': 'User updated successfully'}), 200
