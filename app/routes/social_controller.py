from app import app
from app.controllers.social_controller import add_follow, add_unfollow, get_social

app.route('/follow', methods=['POST'])(add_follow)
app.route('/unfollow', methods=['POST'])(add_unfollow)
app.route('/user/social/<id>', methods=['GET'])(get_social)

