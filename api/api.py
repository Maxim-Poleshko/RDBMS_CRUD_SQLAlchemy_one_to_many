from flask import Blueprint, request, json
from flask.views import MethodView

from homework.app_database import DB

from homework.shema import owner_schema, owners_schema
from homework.model import Owners

USER_API = Blueprint('USER_API', __name__, static_folder='../../static', template_folder='../../template')

class UserView(MethodView):
    """
    CRUD view
    """
    def get(self):
        user = Owners.query.order_by(Owners.id).all()
        return owners_schema.jsonify(user)

    def post(self):
        data = json.loads(request.data.decode())
        new_user = Owners(**data)

        DB.session.add(new_user)
        DB.session.commit()
        return owner_schema.jsonify(data)

    def get_one_user(self, id):
        user = Owners.query.filter_by(id=id).first()
        return owners_schema.jsonify(user)

USER_API.add_url_rule('/user', view_func=UserView.as_view('USER_API'))
USER_API.add_url_rule('/user/<id>', view_func=UserView.as_view('user_change'))
