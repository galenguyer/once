from once import once
from flask import request, jsonify


@once.route("/api/v1/secrets/<id>", methods=["POST"])
def _post_api_v1_secrets(id):
    if request.json is None:
        return jsonify({"error": "data is not recognized as valid json"}), 400
    return jsonify({"id": id})


@once.route("/api/v1/secrets", methods=["GET"])
def _get_api_v1_secrets():
    return "", 204
