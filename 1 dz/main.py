import json
import xmltodict


class Auto(object):
    def __init__(self, brand, model, mileage, state_number, owner, year, engine, price, accident=None, category='car',equipment='normal'):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.state_number = state_number
        self.owner = owner
        self.year = year
        self.price = price
        self.accident = accident
        self.category = category
        self.engine = engine
        self.equipment = equipment


class Owner(object):
    def __init__(self, name, number, email, data):
        self.name = name
        self.number = number
        self.email = email
        self.data = data


class Accident(object):
    def __init__(self, date, quantity, state_numbers):
        self.date = date
        self.quantity = quantity
        self.state_numbers = state_numbers


class Engine(object):
    def __init__(self, horsepower, capacity=1.6, fuel='petrol', turbo=None):
        self.horsepower = horsepower
        self.capacity = capacity
        self.fuel = fuel
        self.turbo = turbo


class Equipment(object):
    def __init__(self, multiwheel=None, multimedia=None, conditioning=None, numberseats=4, bodykit='normal'):
        self.multiwheel = multiwheel
        self.multimedia = multimedia
        self.conditioning = conditioning
        self.numberseats = numberseats
        self.bodykit = bodykit


class Car_market(object):
    def __init__(self, address, site, name, price, auto, rating='5.0'):
        self.address = address
        self.site = site
        self.name = name
        self.price = price
        self.auto = auto
        self.rating = rating


class DataBase(object):
    def __init__(self, car_markets):
        self.car_markets = car_markets


engine1 = Engine(156, 1.6)
engine2 = Engine(208, 2.0)
equipment = Equipment()
owner1 = Owner('Sergey', 888888, 'segey@mail.ru', '01.06.2000')
owner2 = Owner('Olga', 777777, 'olgay@mail.ru', '01.06.2000')
owner3 = Owner('Ann', 666666, 'ann@mail.ru', '01.06.2000')
owner4 = Owner('Oleg', 555555, 'oleg@mail.ru', '01.06.2000')
car1 = Auto('Audi', 'A4', 10000, 'н163сс34', owner1, 2019, engine2, 2100000)
car2 = Auto('LADA', 'priora', 100000, 'о585оо13', owner2, 2008, engine1, 240000)
car3 = Auto('Renault', 'Duster', 70000, 'о001оо56', owner3, 2019, engine2, 1240000)
car4 = Auto('Renault', 'Logan', 100000, 'е450ое65', owner4, 2008, engine1, 240000)
car5 = Auto('Renault', 'Logan', 100000, 'а555аа77', owner1, 2008, engine1, 210000)
carmarket1 = Car_market('Volgograd', 'auto.volgograd', 'Volga', 5000, [car1, car2, car3])
carmarket2 = Car_market('Kazan', 'auto.kazan', 'Kazanka', 6000, [car4, car5])
data_base = DataBase([carmarket1, carmarket2])


def serialised_json(data_base):
    r = json.dumps(data_base, default=lambda x: x.__dict__, ensure_ascii=False)
    with open('db.json', 'w', encoding='utf-8') as f:
        f.write(r)


def deserialised_json():
    with open("db.json", "r") as read_file:
        string = read_file.read()
    data_base = json.loads(string)
    return data_base


def serialised_xml(data_base):
    json_db = json.dumps(data_base, default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
    xml_db = xmltodict.unparse({'xml_db': json.loads(json_db)}, pretty=True)
    with open("db.xml", "w") as write_file:
        write_file.write(xml_db)


def deserialised_xml():
    with open("db.xml", "r") as read_file:
        string = read_file.read()
    data_base = xmltodict.parse(string)['xml_db']
    return data_base
