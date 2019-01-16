from homework.app_database import DB

class Owners(DB.Model):
    """main model"""
    __tablename__ = 'owners'
    id = DB.Column(DB.INTEGER, primary_key=True)
    name = DB.Column(DB.String(80))
    age = DB.Column(DB.INTEGER)
    address = DB.Column(DB.String(80))
    car_car = DB.relationship('aboutCar', backref='carrier')

    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address


class aboutCar(DB.Model):
    """one to many relation"""
    __tablename__ = 'about_car'
    id = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    model = DB.Column(DB.String(80))
    year = DB.Column(DB.Integer)
    price = DB.Column(DB.Integer)
    carrier_id = DB.Column(DB.Integer, DB.ForeignKey('owners.id'))

    def __init__(self, year, price, model):
        self.year = year
        self.price = price
        self.model = model
