from flask import Flask

from app.routes import bp
from app.storage import init_db


def create_app():
    app = Flask(__name__)
    init_db()
    app.register_blueprint(bp)
    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8090)
