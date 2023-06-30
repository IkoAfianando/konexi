from flask import jsonify, request
from app.repositories.post_repository import PostRepository
from app.repositories.post_transaction_repository import PostTransactionRepository
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.service import upload_file

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
    comments = post['comments']
    result = {
        'id': id,
        'title': title,
        'image': image,
        'description': description,
        'likes': likes,
        'comments': comments,
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
        })
    return jsonify(result), 200


@jwt_required()
def add_post():
    user_id = get_jwt_identity()
    image = request.files['image'] if 'image' in request.files else None

    title = request.form.get('title')
    description = request.form.get('description')

    if title is None or title == '' or description is None or description == '':
        return jsonify({'message': 'Title and description are required'}), 400

    post_repo = PostRepository()
    existing_post = post_repo.get_by_title(title)

    if existing_post:
        return jsonify({'message': 'Title already exists'}), 400

    if image is not None:
        destination = image.filename if image else None
        url = upload_file(image, destination, 'belajar-upload')
    else:
        url = None

    new_post = post_repo.create(url, title, description, user_id)
    return jsonify({'message': 'Post created successfully'}), 201


@jwt_required()
def update_post(id):
    user_id = get_jwt_identity()

    image = request.files['image'] if 'image' in request.files else None

    title = request.form.get('title')
    description = request.form.get('description')

    update_repo = PostRepository()
    get_by_id = update_repo.get_by_id(id)

    if user_id != get_by_id['user_id']:
        return jsonify({'message': 'You are not authorized to update this post'}), 401

    if image is not None:
        destination = image.filename if image else None
        url = upload_file(image, destination, 'belajar-upload')
    else:
        url = get_by_id['image']

    update_repo = update_repo.update_post(id, url, title, description)

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


@jwt_required()
def add_like_in_post(id):
    user_id = get_jwt_identity()
    post_id = id

    post_repo = PostRepository()
    post_repo_transaction = PostTransactionRepository()

    post = post_repo.get_by_id(id)

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    exist_like = post_repo_transaction.get_by_user_and_post_id_like(user_id, post_id)

    if exist_like:
        return jsonify({'message': 'You already liked this post'}), 400

    post_repo_transaction.create(user_id, post_id, 'like')
    post_repo_transaction.delete_unlike(user_id, post_id)
    create_like = post_repo.update_likes(id)
    return jsonify({'message': 'Like created successfully'}), 201


@jwt_required()
def add_unlike_in_post(id):
    user_id = get_jwt_identity()
    post_id = id

    post_repo = PostRepository()
    post_repo_transaction = PostTransactionRepository()

    post = post_repo.get_by_id(id)

    if post is None:
        return jsonify({'message': 'Post not found'}), 404

    exist_unlike = post_repo_transaction.get_by_user_and_post_id_unlike(user_id, post_id)
    if exist_unlike:
        return jsonify({'message': 'You already unliked this post'}), 400

    post_repo_transaction.create(user_id, post_id, 'unlike')
    post_repo_transaction.delete_like(user_id, post_id)
    create_like = post_repo.update_unlikes(id)
    return jsonify({'message': 'Unlike created successfully'}), 201

@jwt_required()
def add_comment(id):
    post_id = id
    comment = request.json['comment']
    post_repo = PostRepository()
    post_repo.add_comment(post_id, comment)
    return jsonify({'message': 'Comment created successfully'}), 201

