from bson import ObjectId

from app import mongo


class PostTransactionRepository:
    def __init__(self):
        self.collection = mongo.db.post_transactions

    def create(self, user_id, post_id, transaction_type):
        return self.collection.insert_one(
            {'user_id': user_id, 'post_id': post_id, 'transaction_type': transaction_type}).inserted_id

    def get_by_user_id(self, user_id):
        return self.collection.find_one({'user_id': user_id})

    def get_by_post_id(self, post_id):
        return self.collection.find_one({'post_id': post_id})

    def get_by_user_and_post_id(self, user_Id, post_id):
        return self.collection.find_one({'user_id': user_id, 'post_id': post_id})
