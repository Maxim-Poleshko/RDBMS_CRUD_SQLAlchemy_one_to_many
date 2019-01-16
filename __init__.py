from flask import Flask

from homework.api.api import USER_API
from homework.app_database import DB, MA
from homework.config import runtime_config
from homework.keyspaces.keyspaces import create_db_api
from homework.one_to_many.one_to_many import one_to_many_api

def run_app():
    app = Flask(__name__)
    DB.init_app(app)
    MA.init_app(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(USER_API)
    app.register_blueprint(create_db_api)
    app.register_blueprint(one_to_many_api)
    return app
