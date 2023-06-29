from app import app
from app.controllers.post_controler import add_post, delete_post, update_post, get_post

app.route('/post', methods=['POST'])(add_post)
app.route('/post/<id>', methods=['PUT'])(update_post)
app.route('/post/<id>', methods=['DELETE'])(delete_post)
app.route('/post/<id>', methods=['GET'])(get_post)

