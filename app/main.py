from flask import Flask, render_template
from models import db
from routes.users import user_routes
from routes.workshops import workshop_routes
from routes.notifications import notification_routes
from flask_cors import CORS



app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@postgres:5432/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


# Register Blueprints
app.register_blueprint(user_routes, url_prefix="/users")
app.register_blueprint(workshop_routes, url_prefix="/workshops")
app.register_blueprint(notification_routes, url_prefix="/notifications")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)

