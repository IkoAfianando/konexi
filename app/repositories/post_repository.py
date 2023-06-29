from bson import ObjectId

from app import mongo


class PostRepository:
    def __init__(self):
        self.collection = mongo.db.posts

    def find_by_title(self, title):
        return self.collection.find({"title": f"/.*{title}.*/"})

    def get_by_title(self, title):
        return self.collection.find_one({"title": title})

    def get_by_id(self, user_id):
        return self.collection.find_one({'_id': ObjectId(user_id)})

    def create(self, image, title, description, user_id):
        return self.collection.insert_one({'image': image, 'title': title, 'description': description,
                                           'post_data': {'likes': 0, 'unlikes': 0}, 'user_id': user_id}).inserted_id

    def update_post(self, post_id, image, title, description):
        return self.collection.update_one({'_id': ObjectId(post_id)},
                                          {'$set': {'image': image, 'title': title, 'description': description}})

    def delete(self, post_id):
        return self.collection.delete_one({'_id': ObjectId(post_id)})

    def update_likes(self, post_id, likes):
        return self.collection.update_one({'_id': ObjectId(post_id)}, {'$set': {'post_data.likes': likes}})

    def update_unlikes(self, post_id, unlikes):
        return self.collection.update_one({'_id': ObjectId(post_id)}, {'$set': {'post_data.unlikes': unlikes}})
