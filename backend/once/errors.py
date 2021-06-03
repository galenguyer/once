from once import once
from flask import request, jsonify


@once.errorhandler(400)
def _error_400(error):
    return jsonify({"error": "bad request", "details": str(error)}), 400


@once.errorhandler(404)
def _error_404(error):
    return jsonify({"error": "not found"}), 404
