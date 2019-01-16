from flask import Blueprint
from flask.views import MethodView

from homework.model import Owners
from homework.shema import owner_schema, owners_schema

one_to_many_api = Blueprint('one_to_many', __name__, static_folder='../../static', template_folder='../../template')


class NamesView(MethodView):
    """
    View owners by id
    """
    def get(self):
        names = Owners.query.first()
        print(names.car_car)
        return owner_schema.jsonify(names)

one_to_many_api.add_url_rule('/one_to_many_names', view_func=NamesView.as_view('one_to_many_names'))
