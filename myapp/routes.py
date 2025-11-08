from flask import jsonify


def register_routes(app):
    @app.route("/")
    def index():
        return "Hello from Flask CI CD app"

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/api/data")
    def get_data():
        data = {"items": [1, 2, 3], "message": "Sample data"}
        return jsonify(data)
