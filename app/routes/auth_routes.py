from app import app
from app.controllers.auth_controller import register, login

app.route('/register', methods=['POST'])(register)
app.route('/login', methods=['POST'])(login)
