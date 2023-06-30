from bson import ObjectId

from app import mongo


class PostTransactionRepository:
    def __init__(self):
        self.collection = mongo.db.post_transactions

    def create(self, user_id, post_id, transaction_type):
        return self.collection.insert_one(
            {'user_id': user_id, 'post_id': post_id, 'transaction_type': transaction_type}).inserted_id
    def get_by_user_and_post_id_like(self, user_id, post_id):
        print(user_id, post_id)
        return self.collection.find_one({'user_id': user_id, 'post_id': post_id, 'transaction_type': 'like'})

    def get_by_user_and_post_id_unlike(self, user_id, post_id):
        return self.collection.find_one({'user_id': user_id, 'post_id': post_id, 'transaction_type': 'unlike'})

    def delete_like(self, user_id, post_id):
        return self.collection.delete_one({'user_id': user_id, 'post_id': post_id, 'transaction_type': 'like'})

    def delete_unlike(self, user_id, post_id):
        return self.collection.delete_one({'user_id': user_id, 'post_id': post_id, 'transaction_type': 'unlike'})