# 01 basic class and objects
# create a car class , with attributes brand and model , and create an instance of it

class Car:
    # brand=None
    # model=None
    def __init__(self , brand , model):
        self.brand = brand
        self.model= model

# my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)

class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model= model
    def full_name(self):
        return self.brand+self.model

# my_car = Car("Toyota" , "Corolla")
# print(my_car.full_name())

# Inheritance , create an electric car class,and add an extra attribute battery size

class ElectricClass(Car):
    def __init__(self , brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car_1 = ElectricClass("Tesla" , "ModelS" , "85kwh")
print(my_car_1.model)
