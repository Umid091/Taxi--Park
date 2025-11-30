from idlelib.run import manage_socket
from itertools import count
from mimetypes import inited


class Car:
    def __init__(self, model,brand,year,seria):
        self.model = model
        self.year = year
        self.brand = brand
        self.seria=seria
        self.is_active = True
        self.is_bron = False
        self.bron_by = None



class User:
    def __init__(self, name, phone, age, seria,password):
        self.name = name
        self.phone = phone
        self.age = age
        self.seria = seria
        self.is_active=True
        self.password = password
        self.is_admin = False


class Order:
    def __init__(self,user_id,car_id,data_start,data_end):
        self.user_id=user_id
        self.car_id=car_id
        self.data_start=data_start
        self.data_end=data_end


class Park:
    def __init__(self,title):
        self.title=title
        self.users=[]
        self.cars=[]
        self.orders=[]

    def add_car(self):
        try:

            model=input("model:")
            brand=input("brand:")
            year=input("year:")
            seria=int(input("seria:"))
            car1=Car(model,brand,year,seria)
            self.cars.append(car1)
            print(f"🚗✅ {model} avtomabili qo'shildi!!")
        except ValueError:
            print("\033[91m❌ Mashina qo'shilmadi malumotlar xato!! \n       QAYTA URINB KO'RING  \033[0m")




    def delete_car(self):
        seria=int(input("seria raqami:"))
        for i in self.cars:
            if i.seria==seria:
                self.cars.remove(i)
                print("✅Mashina o'chirildi!!")
                return
        print("❌ Bunday seria li mashina mavjud emas yo'q!!")

    def update_car(self):
        seria = int(input("seria raqami:"))
        for i in self.cars:

            if i.seria == seria:
                i.model=input("new model:")
                i.brand=input("new brand:")
                i.year=input("new year:")
                print(f"✅ seriasi={seria} bolgan mashina yangilandi")
                return
        print("❌ Bunday seria li mashina mavjud emas yo'q!!")


    def view_cars(self):
        if not self.cars:
            print("❌ Bazada mashinalar yo'q hali!!!")
            return
        count=1
        for i in self.cars:
            print(f"{count}.model:{i.model} | brand:{i.brand} | year:{i.year} | seroia:{i.seria}")
            count+=1



    def add_user(self):
        try:

            name=input("name:")
            phone=int(input("phone:"))
            age=int(input("age:"))
            seria=int(input("seria:"))
            password=int(input("password:"))
            user1=User(name,phone,age,seria, password)
            self.users.append(user1)
            print(f"🦸✅ {name} Bazaga qo'shildi!! ")
        except ValueError:
            print("\033[91m❌ User qo'shilmadi malumotlar xato!! \n       QAYTA URINB KO'RING  \033[0m")

    def delete_user(self):
        seria=int(input("seria raqami:"))
        for i in self.users:
            if i.seria==seria:
                self.users.remove(i)
                print(f"✅ ism={i.name} bo'gan ishi bazadan o'chirildi!!")
                return
        print("❌ Bunday seria topilmadi!!")


    def update_user(self):
        seria=int(input("seria raqami:"))
        for i in self.users:
            if i.seria==seria:

                i.name=input("new name:")
                i.phone=int(input("new phone:"))
                i.age=int(input("new age:"))
                print(f"seria:{seria} bo'lgan ishchi malumotlri yangilanddi")
                return
        print("❌ seria topilmadi!!")


    def view_users(self):
        if not self.users:
            print("❌ Bazada user yo'q!!!")
            return
        count=1
        for i in self.users:
            print(f"{count}.name:{i.name} | phone:{i.phone} | age:{i.age}")
            count+=1

    def add_oder(self):
        user_id = int(input("user seria: "))
        for i in self.users:
            if i.seria == user_id:
                if i.is_active == False:
                    print("❌ User bloklangan!")
                    return

                car_id = int(input("car seria: "))

                car_found = False
                for j in self.cars:
                    if j.seria == car_id:
                        car_found = True
                        if j.is_active == False:
                            print("❌ Car bloklangan!")
                        else:
                            data_start = input("start date: ")
                            data_end = input("end date: ")
                            order1 = Order(user_id, car_id, data_start, data_end)
                            self.orders.append(order1)
                            print("Order qo'shildi!")
                            return
                if not car_found:
                    print("❌ Bunday mashina topilmadi!")
                    return
        else:
            print("❌ Bunday user topilmadi!")

    def user_blok(self):
        seria=int(input("seria raqami:"))
        for i in self.users:
            if i.seria==seria:
                i.is_active=False
                print("✅ User Bloklandi")
                user_id=seria
                for j in self.orders:
                    if j.user_id==user_id:
                        self.orders.remove(j)
                        print(f"✅ name:{i.name} ishchi olib tashlandi!!")
                        return
                    else:
                        return print(f"❌bunday user_id yo'q")
        print("❌Bunnday seria mavjud emas!!")



    def view_order(self):
        if not self.orders:
            print("❌ Bazada order yo'q!!!")
            return
        count=1
        for i in self.orders:
            print(f"{count}.user_id:{i.user_id} | car_id:{i.car_id} | data_start:{i.data_start} | data_and:{i.data_end}")
            count+=1


    def all_info(self):
        print(f"Park nomi: {self.title}")
        print(f"Cars:{len(self.cars)} ta")
        print(f"Users:{len(self.users)} ta")
        print(f"Orders:{len(self.orders)} ta")

    def bron_car(self):
        try:
            user_id = int(input("user seria:"))
        except ValueError:
            return ("❌ Xato! Seria faqat RAQAM bo‘lishi kerak")
        try:
            car_id = int(input("car seria:"))
        except ValueError:
            return print("❌ Xato! Seria faqat RAQAM bo‘lishi kerak!")

        for user in self.users:
            if user.seria == user_id:
                for car in self.cars:
                    if car.seria == car_id:
                        if car.is_bron == False:
                            car.is_bron = True
                            car.bron_by = user.name
                            return print(f"✅ {car.model} mashinasi {user.name} tomonidan BRON qilindi!")
                        else:
                            return print(f"❌ Bu mashina allaqachon {car.booked_by} tomonidan bron qilingan!")
                    else:
                        print("❌ Bunday mashina topilmadi")
                return
        print("❌ User topilmadi!")

    def confirm_bron_admin(self):
        try:
            car_id = int(input("Car seria: "))
        except ValueError:
            return print("❌ Xato! Seria faqat RAQAM bo‘lishi kerak!")

        for car in self.cars:
            if car.seria == car_id:
                car.is_active = True
                car.is_bron = False
                print(f"✅ ADMIN tasdiqladi! Mashina: {car.model} rasmiy faol!")
                return
            else:
                print("❌ Bunday mashina topilmadi!")

    def login(self):
        try:
            name = input("username: ")
            password = int(input("password: "))
        except ValueError:
            print("\033[91m❌ Password yoki Name xato!!\033[0m")
            return None, False

        for item in self.users:
            if item.name == name and item.password == password:
                return item, True

        print("\033[91m❌ Login yoki Parol xato!!\033[0m")
        return None, False


park=Park("FastTaxi 🚕")
admin = User('admin', 123456, 1234, 12,000)
admin.is_admin = True
park.users.append(admin)

def driver_manger(s:Park):
    while True:
        kod=input("1.update_user \n 2.view_cars \n 3.bron_car:")
        if kod=="1":
            s.update_user()
        elif kod=="2":
            s.view_cars()
        elif kod=="3":
            s.bron_car()
        else:
            break

def admin_manger(p:Park):
    while True:
        kod=input("========Park Manager======== \n 1.add_car \n 2.delete_car \n 3.update_car \n 4.view_cars \n 5.add_user \n 6.delete_user \n 7.update_user \n 8.view_user \n 9.add_order \n 10.view_order \n 11.user_blok \n 12.all_info \n 13.confirm_bron_admin \n 14.park_manger:")
        if kod=="1":
            p.add_car()
        elif kod=="2":
            p.delete_car()
        elif kod=="3":
            p.update_car()
        elif kod=="4":
            print("---------------------------------------------")
            p.view_cars()
            print("---------------------------------------------")
        elif kod=="5":
            p.add_user()
        elif kod=="6":
            p.delete_user()
        elif kod=="7":
            p.update_user()
        elif kod=="8":
            print("---------------------------------------------")
            p.view_users()
            print("---------------------------------------------")
        elif kod=="9":
            p.add_oder()
        elif kod=="10":
            print("---------------------------------------------")
            p.view_order()
            print("---------------------------------------------")
        elif kod=="11":
            p.user_blok()
        elif kod=='12':
            print("---------------------------")
            p.all_info()
            print("---------------------------")
        elif kod=="13":
            p.confirm_bron_admin()
        elif kod=="14":
            park_manager(park)
        else:
            break



# park_manger(park)

def park_manager(p: Park):
    while True:
        user = p.login()

        if user[0] is None:
            break

        if user[0].is_admin:
            admin_manger(p)

        else:
            driver_manger(p)

park_manager(park)



































