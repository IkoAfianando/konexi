from flask import jsonify, request
from app.repositories.user_repository import UserRepository
from app.repositories.social_repository import SocialRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

@jwt_required()
def add_follow():
    user_id = get_jwt_identity()
    user_target_id = request.json['user']

    if user_id == user_target_id:
        return jsonify({'message': 'You cannot follow yourself'}), 400

    social_repository = SocialRepository()
    user_repository = UserRepository()

    existing_follower = social_repository.get_by_user_and_user_target_id(user_id, user_target_id)
    if existing_follower:
        return jsonify({'message': 'You already follow this user'}), 400

    user_repository.insert_follower(user_target_id)
    user_repository.insert_following(user_id)

    social_repository.create(user_id, user_target_id)
    return jsonify({'message': 'success'}), 200

@jwt_required()
def add_unfollow():
    user_id = get_jwt_identity()
    user_target_id = request.json['user']

    if user_id == user_target_id:
        return jsonify({'message': 'You cannot unfollow yourself'}), 400

    social_repository = SocialRepository()
    user_repository = UserRepository()

    existing_follower = social_repository.get_by_user_and_user_target_id(user_id, user_target_id)
    if not existing_follower:
        return jsonify({'message': 'You do not follow this user'}), 400

    user_repository.remove_follower(user_target_id)
    user_repository.remove_following(user_id)

    social_repository.delete(user_id, user_target_id)
    return jsonify({'message': 'success'}), 200

@jwt_required()
def get_social(id):
    user_id = get_jwt_identity()
    user_repository = UserRepository()

    data = user_repository.get_by_id(id)
    if not data:
        return jsonify({'message': 'User not found'}), 404


    result = {
        'username': data['username'],
        'following': data['social']['following'],
        'follower': data['social']['follower'],
    }
    return jsonify(result), 200


