from flask import Flask, request, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for sessions

# MongoDB connection
# client = pymongo.MongoClient("mongodb://localhost:27017/")                
client = pymongo.MongoClient("mongodb://host.docker.internal:27017/") 
db = client["devops"]

@app.route('/signup', methods=['POST'])
def signup():
    data = request.form
    email = data['email']
    password = data['password']

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Store the user in the database
    db.users.insert_one({
        "email": email,
        "password": hashed_password
    })

    return jsonify({"message": "User signed up successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    email = data['email']
    password = data['password']

    # Find the user in the database
    user = db.users.find_one({"email": email})

    if user and check_password_hash(user['password'], password):
        # Store user's email in session
        session['email'] = email
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid email or password"})

@app.route('/logout')
def logout():
    # Clear the session
    session.clear()
    return jsonify({"message": "Logged out successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000, debug=True)
