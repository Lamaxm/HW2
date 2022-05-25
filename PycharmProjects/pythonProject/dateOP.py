class Vehicle :
    def __init__(self ,brand,name,color,capacity,plant_number):
        self.name = name
        self.color = color
        self.brand = brand
        self.capacity = capacity
        self.plant_number = plant_number
    def drive(self):
        print("the vehicle_name is driving!")
    def drift(self):
        print("the vehicle_name is drifting !!")
    def carry_cargo(self):
        print("the vehicle_name is carrying cargo !!")
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_brand(self,brand):
        self.brand= brand
    def get_brand(self):
        return self.brand
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_plate_number(self,plate_number):
        self.plant_number=plate_number
    def get_plate_number(self):
        return self.plant_number
    def set_capacity(self,capacity):
        self.capacity = capacity
    def get_capacity(self):
        return self.capacity

class Bus(Vehicle):
    def number_student(self):
        print('this bus can accommodate 100 student')
class Truck(Vehicle):
    def carry(self):
        print('this Truck carries 1000 kg')

Vehicle1 = Vehicle('toyota','car1','black',5,123)
Bus1 = Bus('blxbus','bus1','yellow',101,456)
Truck1 = Truck('scana','Truck','brown',2,789)

Vehicle1.drive()
Bus1.number_student()
Truck1.carry()