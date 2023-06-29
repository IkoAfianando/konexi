from app import app
from app.controllers.post_controler import add_post, delete_post, update_post, get_post_by_id, get_posts

app.route('/post', methods=['POST'])(add_post)
app.route('/post/<id>', methods=['PUT'])(update_post)
app.route('/post/<id>', methods=['DELETE'])(delete_post)
app.route('/post/<id>', methods=['GET'])(get_post_by_id)
app.route('/posts', methods=['GET'])(get_posts)

