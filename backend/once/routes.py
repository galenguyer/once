from once import once
from flask import request, jsonify


@once.route("/api/v1/create", methods=["POST"])
def _post_api_v1_create():
    if request.json is None:
        return jsonify({"error": "data is not recognized as valid json"}), 400
    return "", 204
