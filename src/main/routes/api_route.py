from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.composer import register_person_composer
from src.main.composer import register_user_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/people", methods=["POST"])
def register_person():
    """Represents the route used to register a new person"""

    message = {}
    response = flask_adapter(request, api_route=register_person_composer())

    if response.status_code < 300:
        message = {
            "type": "people",
            "tax_id_number": response.body.tax_id_number,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """Represents the route used to register a new user"""

    message = {}
    response = flask_adapter(request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {
                "username": response.body.username,
                "email": response.body.email,
            },
            "relationships": {
                "person": {
                    "type": "people",
                    "tax_number_id": response.body.person_tax_id,
                }
            },
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
