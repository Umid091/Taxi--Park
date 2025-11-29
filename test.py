class User:
    def __init__(self, name, phone, seria, age):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = 0000
        self.is_active = True
        self.is_admin = False


class Car:
    def __init__(self, model, brand, year, seria, ):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_active = True


class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True


class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []

    def login(self):
        name = input("username: ")
        password = int(input("password: "))
        for item in self.users:
            if item.username == name and item.password == password:
                return item, True
        return 1, False


park = Park('park1')
admin = User('admin', 123456, 1234, 12)
admin.is_admin = True
park.users.append(admin)


def park_manager(p: Park):
    user = p.login()
    if user[1]:
        pass


park_manager(park)
