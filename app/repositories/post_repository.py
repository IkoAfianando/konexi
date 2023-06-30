from bson import ObjectId

from app import mongo
import re


class PostRepository:
    def __init__(self):
        self.collection = mongo.db.posts

    def find_by_title(self, title):
        rgx = re.compile('.*' + title + '.*', re.IGNORECASE)

        return self.collection.find({'title': rgx})

    def get_by_title(self, title):
        return self.collection.find_one({"title": title})

    def get_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def get_posts(self):
        return self.collection.find()

    def create(self, image, title, description, user_id):
        return self.collection.insert_one({'image': image, 'title': title, 'description': description,
                                           'post_data': {'likes': 0}, 'user_id': user_id, 'comments': []}).inserted_id

    def update_post(self, post_id, image, title, description):
        return self.collection.update_one({'_id': ObjectId(post_id)},
                                          {'$set': {'image': image, 'title': title, 'description': description}})

    def delete(self, post_id):
        return self.collection.delete_one({'_id': ObjectId(post_id)})

    def get_likes(self, post_id):
        return self.collection.find_one({'_id': ObjectId(post_id)})

    def update_likes(self, post_id):
        like = self.collection.find_one({'_id': ObjectId(post_id)})
        likes = like['post_data']['likes']

        return self.collection.update_one({'_id': ObjectId(post_id)}, {'$set': {'post_data.likes': likes + 1}})

    def update_unlikes(self, post_id):
        like = self.collection.find_one({'_id': ObjectId(post_id)})
        likes = like['post_data']['likes']
        return self.collection.update_one({'_id': ObjectId(post_id)}, {'$set': {'post_data.likes': likes - 1}})

    def add_comment(self, post_id, comment):
        return self.collection.update_one({'_id': ObjectId(post_id)}, {'$push': {'comments': comment}})
