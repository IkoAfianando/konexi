from app import app

# app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb+srv://doadmin:89xun34f6rF0k12X@db-mongodb-sgp1-06303-1fa69bf3.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-06303'  # Ganti dengan URL MongoDB Anda
# app.config['SECRET_KEY'] = 'mysecretkey'  # Ganti dengan kunci rahasia Anda
#
# mongo = PyMongo(app)
# bcrypt = Bcrypt(app)
#
# # Fungsi untuk mengenkripsi password
# def hash_password(password):
#     return bcrypt.generate_password_hash(password).decode('utf-8')
#
# # Fungsi untuk membandingkan password terenkripsi dengan password asli
# def check_password(password, hashed_password):
#     return bcrypt.check_password_hash(hashed_password, password)
#
# # Route untuk registrasi pengguna baru
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']
#
#     # Periksa apakah pengguna sudah terdaftar
#     if mongo.db.users.find_one({'username': username}):
#         return jsonify({'message': 'Username already exists'})
#
#     # Enkripsi password
#     hashed_password = hash_password(password)
#
#     # Simpan pengguna ke database
#     user = {'username': username, 'password': hashed_password}
#     mongo.db.users.insert_one(user)
#
#     return jsonify({'message': 'User registered successfully'})
#
# # Route untuk login
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']
#
#     # Periksa apakah pengguna terdaftar
#     user = mongo.db.users.find_one({'username': username})
#     if not user:
#         return jsonify({'message': 'User not found'})
#
#     # Periksa kecocokan password
#     if not check_password(password, user['password']):
#         return jsonify({'message': 'Invalid credentials'})
#
#     return jsonify({'message': 'Logged in successfully'})

if __name__ == '__main__':
    app.run(debug=True)
