from once import once

@once.route("/api/v1/create", methods=["POST"])
def _post_api_v1_create():
    return "", 204
