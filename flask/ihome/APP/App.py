from flask import Flask
from APP.settings import templates_dir, static_dir
from APP.functions import init_ext
from APP.url_regist import blue_regist


def create_app(config):
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    blue_regist(app)
    app.config.from_object(config)
    init_ext(app)

    return app
