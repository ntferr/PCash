from app import app


if __name__ == "__main__":
    app.run(debug=True)


cors = CORS(app, resources = {r"/api/*": {"origins": "*"}})