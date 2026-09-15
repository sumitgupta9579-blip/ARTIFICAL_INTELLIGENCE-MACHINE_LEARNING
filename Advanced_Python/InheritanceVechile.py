class Vechile():
    def __init__(self,brand):
        self.brand=brand
    def display_brand(self):
        print(self.brand)

class Car(Vechile):
    # pass
    car_engine = "kia_1"

c1=Car("Honda")
c1.display_brand()

c2 = Car("Kia")
c2.display_brand()

print(c2.car_engine)

