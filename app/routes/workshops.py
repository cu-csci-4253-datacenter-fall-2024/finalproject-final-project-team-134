from flask import Blueprint, request, jsonify
from models import db, Workshop

workshop_routes = Blueprint('workshops', __name__)

@workshop_routes.route("/", methods=["GET"])
def list_workshops():
    workshops = Workshop.query.all()
    print("Workshops fetched:", workshops)
    return jsonify([{"id": w.id, "title": w.title, "location": w.location, "price": w.price} for w in workshops])

@workshop_routes.route("/create", methods=["POST"])
def create_workshop():
    data = request.json
    workshop = Workshop(
        title=data["title"], description=data["description"],
        location=data["location"], price=data["price"]
    )
    db.session.add(workshop)
    db.session.commit()
    return jsonify({"message": "Workshop created successfully!"})

