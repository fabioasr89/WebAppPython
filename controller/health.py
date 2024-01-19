from flask import Blueprint,Response,jsonify

healt_flask=Blueprint('health_flask',__name__)

@healt_flask.route("/health")
def health():
    return "200"