from homework.app_database import MA # this is marshmallow


class OwnersSchema(MA.Schema):
    class Meta:

        fields = ('id', 'name', 'age', 'address')


owner_schema = OwnersSchema()
owners_schema = OwnersSchema(many=True)


class CarsSchema(MA.Schema):
    class Meta:

        fields = ('id', 'model')


car_schema = CarsSchema()
cars_schema = CarsSchema(many=True)

class aboutCarSchema(MA.Schema):
    class Meta:

        fields = ('id', 'year', 'price', 'model_id')

about_car = aboutCarSchema()
about_cars = aboutCarSchema(many=True)