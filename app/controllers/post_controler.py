from flask import jsonify, request
from app.repositories.post_repository import PostRepository
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def get_post_by_id(id):
    post_repo = PostRepository()
    post = post_repo.get_by_id(id)

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    id = str(post['_id'])
    title = post['title']
    image = post['image']
    description = post['description']
    likes = post['post_data']['likes']
    unlikes = post['post_data']['unlikes']
    result = {
        'id': id,
        'title': title,
        'image': image,
        'description': description,
        'likes': likes,
        'unlikes': unlikes
    }
    return jsonify(result), 200

@jwt_required()
def get_posts():
    query_title = request.args.get('title')

    post_repo = PostRepository()

    if query_title is not None:
        data = post_repo.find_by_title(query_title)
    else:
        data = post_repo.get_posts()


    result = []
    for post in data:
        result.append({
            'id': str(post['_id']),
            'title': post['title'],
            'image': post['image'],
            'description': post['description'],
            'likes': post['post_data']['likes'],
            'unlikes': post['post_data']['unlikes']
        })
    return jsonify(result), 200

@jwt_required()
def add_post():
    user_id = get_jwt_identity()
    image_file = request.files['image_file'] if 'image_file' in request.files else None

    image = request.form.get('image')
    title = request.form.get('title')
    description = request.form.get('description')

    if title is None or title == '' or description is None or description == '' or image is None or image == '':
        return jsonify({'message': 'Title and description are required'}), 400

    post_repo = PostRepository()
    existing_post = post_repo.get_by_title(title)

    if existing_post:
        return jsonify({'message': 'Title already exists'}), 400

    new_post = post_repo.create(image, title, description, user_id)
    return jsonify({'message': 'Post created successfully'}), 201


@jwt_required()
def update_post(id):
    user_id = get_jwt_identity()

    image_file = request.files['image_file'] if 'image_file' in request.files else None

    image = request.form.get('image')
    title = request.form.get('title')
    description = request.form.get('description')

    update_repo = PostRepository()
    get_by_id = update_repo.get_by_id(id)

    if user_id != get_by_id['user_id']:
        return jsonify({'message': 'You are not authorized to update this post'}), 401

    update_repo = update_repo.update_post(id, image, title, description)

    return jsonify({'message': 'Post updated successfully'}), 200


@jwt_required()
def delete_post(id):
    user_id = get_jwt_identity()

    delete_repo = PostRepository()
    get_by_id = delete_repo.get_by_id(id)

    if user_id != get_by_id['user_id']:
        return jsonify({'message': 'You are not authorized to delete this post'}), 401

    delete_repo.delete(id)

    return jsonify({'message': 'Post deleted successfully'}), 200
