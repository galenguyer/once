from once import once
from flask import request, jsonify


@once.route("/api/v1/secrets", methods=["POST"])
def _post_api_v1_secrets():
    if request.json is None:
        return jsonify({"error": "data is not recognized as valid json"}), 400
    return "", 204


@once.route("/api/v1/secrets", methods=["GET"])
def _get_api_v1_secrets():
    return "", 204
