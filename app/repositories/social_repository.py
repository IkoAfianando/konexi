from bson import ObjectId

from app import mongo


class SocialRepository:
    def __init__(self):
        self.collection = mongo.db.users

    def create(self, user_id, transaction_type, user_target_id):
        return self.collection.insert_one({'user_id': user_id, 'transaction_type': transaction_type, 'user_target_id': user_target_id}).inserted_id


    def get_by_user_and_user_target_id(self, user_id, user_target_id):
        return self.collection.find_one({'user_id': user_id, 'user_target_id': user_target_id})
