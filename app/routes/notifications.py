from flask import Blueprint, request, jsonify
from google.cloud import pubsub_v1
import json

notification_routes = Blueprint('notifications', __name__)

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
TOPIC_NAME = "projects/voltaic-talent-439403-q6/topics/test-topic"
SUBSCRIPTION_NAME = "projects/voltaic-talent-439403-q6/subscriptions/test-sub"

@notification_routes.route("/send", methods=["POST"])
def send_notification():
    try:
        data = request.json
        message = json.dumps(data)
        print(f"Sending message: {message}")
        publisher.publish(TOPIC_NAME, message.encode("utf-8"))
        return jsonify({"message": "Notification sent successfully!"}), 200
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

@notification_routes.route("/receive", methods=["GET"])
def receive_notifications():
    def callback(message):
        print(f"Received message: {message.data.decode('utf-8')}")
        message.ack()

    try:
        subscriber.subscribe(SUBSCRIPTION_NAME, callback=callback)
        return jsonify({"message": "Listening for messages..."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500