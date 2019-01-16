from flask import Blueprint
from flask.views import MethodView

from homework.app_database import DB

create_db_api = Blueprint('create_db', __name__, static_folder='../../static', template_folder='../../template')


class CreateDatabaseView(MethodView):
    """
    Create database tables
    """
    def post(self):
        DB.create_all()
        DB.session.commit()
        return "Successfully created all tables"


create_db_api.add_url_rule('/keyspaces', view_func=CreateDatabaseView.as_view('create_db_api'))