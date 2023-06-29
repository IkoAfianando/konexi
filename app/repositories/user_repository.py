from bson import ObjectId

from app import mongo


class UserRepository:
    def __init__(self):
        self.collection = mongo.db.users

    def get_by_username(self, username):
        return self.collection.find_one({'username': username})

    def get_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def create(self, username, password):
        return self.collection.insert_one({'username': username, 'password': password}).inserted_id

    def update_password(self, user_id, password):
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'password': password}})
