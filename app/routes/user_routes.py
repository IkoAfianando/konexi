from app import app
from app.controllers.user_controller import update_user, get_user

app.route('/user', methods=['POST'])(get_user)
app.route('/user', methods=['PATCH'])(update_user)

