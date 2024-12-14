from flask import Blueprint, request, jsonify
from models import db, User

user_routes = Blueprint('users', __name__)

@user_routes.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

