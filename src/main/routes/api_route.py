from flask import Blueprint, jsonify, request
from src.main.adapter import flask_adapter
from src.main.composer import register_person_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/people", methods=["POST"])
def register_person():
    """Represents the route used to register a new person"""

    message = {}
    response = flask_adapter(request, api_route=register_person_composer())

    if response.status_code < 300:
        message = {
            "Type": "People",
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
