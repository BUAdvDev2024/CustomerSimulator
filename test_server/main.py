from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello, World!"), 200

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}!"), 200

@app.route('/api/login', methods=['POST'])
def login():
    email = request.json["email"]
    password = request.json["password"]
    if email == "valid_user@gmail.com":
        return jsonify(message="Successful login"), 200
    else:
        return jsonify(message="Invalid login"), 400
    
@app.route('/api/register', methods=['POST'])
def register():
    email = request.json["email"]
    password = request.json["password"]
    if email == "new_user@gmail.com":
        return jsonify(message="Successfuly registed user"), 200
    else:
        return jsonify(message="Email address is already associated with an account"), 400

if __name__ == '__main__':
    app.run(debug=True)
