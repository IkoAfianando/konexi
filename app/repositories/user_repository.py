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
        return self.collection.insert_one({'username': username, 'password': password,
                                           'social': {'follower': 0, 'following': 0}}).inserted_id

    def update_password(self, user_id, password):
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'password': password}})

    def get_followers(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})['social']['follower']

    def get_following(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})['social']['following']

    def insert_follower(self, user_id):
        follower = self.get_followers(user_id)
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'social.follower': follower + 1}})

    def insert_following(self, user_id):
        following = self.get_following(user_id)
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'social.following': following + 1}})

    def remove_follower(self, user_id):
        follower = self.get_followers(user_id)
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'social.follower': follower - 1}})

    def remove_following(self, user_id):
        following = self.get_following(user_id)
        return self.collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'social.following': following - 1}})
