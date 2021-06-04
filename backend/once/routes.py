from once import once, db
from once.models import Secret
from flask import request, jsonify
import secrets


@once.route("/api/v1/secrets/<hash>", methods=["POST"])
def _post_api_v1_secrets(hash):
    # ensure data has some json
    if request.json is None:
        return jsonify({"error": "data is not recognized as valid json"}), 400

    # ensure at the least data was received, as that's all we care about now
    try:
        if len(str(request.json["data"])) < 1:
            return jsonify({"error": "request does not contain any data"}), 400
    except KeyError:
        return jsonify({"error": "request does not contain any data"}), 400

    # validate hash length
    if len(hash) < 8 or len(hash) > 24:
        return jsonify({"error": "hash is of invalid length"}), 400

    id = hash + "".join(secrets.token_hex(8))
    while Secret.query.get(id) is not None:
        id = hash + "".join(secrets.token_hex(8))
    secret = Secret(id=id, data=str(request.json["data"]))
    db.session.add(secret)
    db.session.commit()
    return jsonify(Secret.query.get(id).as_dict())


@once.route("/api/v1/secrets/<id>", methods=["GET"])
def _get_api_v1_secrets(id):
    data = Secret.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(data.as_dict())
