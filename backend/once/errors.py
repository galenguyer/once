from once import once
from flask import request, jsonify


@once.errorhandler(400)
def _error_400(error):
    return jsonify({"error": "bad request", "details": str(error)}), 400
