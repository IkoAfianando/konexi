from app import app
from app.controllers.post_controler import add_post, delete_post, update_post, get_post_by_id, get_posts, add_like_in_post, add_unlike_in_post, add_comment

app.route('/post', methods=['POST'])(add_post)
app.route('/post/<id>', methods=['PUT'])(update_post)
app.route('/post/<id>', methods=['DELETE'])(delete_post)
app.route('/post/<id>', methods=['GET'])(get_post_by_id)
app.route('/posts', methods=['GET'])(get_posts)
app.route('/post/<id>/like', methods=['POST'])(add_like_in_post)
app.route('/post/<id>/comment', methods=['POST'])(add_comment)
app.route('/post/<id>/unlike', methods=['POST'])(add_unlike_in_post)

