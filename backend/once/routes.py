from once import once, db
from once.models import Secret
from flask import request, jsonify


@once.route("/api/v1/secrets/<id>", methods=["POST"])
def _post_api_v1_secrets(id):
    # ensure data has some json
    if request.json is None:
        return jsonify({"error": "data is not recognized as valid json"}), 400

    # ensure at the least data was received, as that's all we care about now
    try:
        if len(str(request.json["data"])) < 1:
            return jsonify({"error": "request does not contain any data"}), 400
    except KeyError:
        return jsonify({"error": "request does not contain any data"}), 400

    secret = Secret(id=id, data=str(request.json["data"]))
    db.session.add(secret)
    db.session.commit()
    return jsonify(Secret.query.get(id).as_dict())


@once.route("/api/v1/secrets", methods=["GET"])
def _get_api_v1_secrets():
    return "", 204
