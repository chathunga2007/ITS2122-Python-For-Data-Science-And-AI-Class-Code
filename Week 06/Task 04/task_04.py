# (i) Parent class named Vehicle
class Vehicle:
    # (iii) Constructor that accepts vehicle_type and initializes it
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    # (ii) Method drive (or drive()) that prints vehicle is driving
    def drive(self):
        print(f"The {self.vehicle_type} is driving.")


# (iv) Child class named Car inherits from Vehicle
class Car(Vehicle):
    # (v) The Car class does not have its own constructor (inherits Vehicle's __init__)

    # (vi) Override the drive method to print "Car is driving"
    def drive(self):
        print("Car is driving.")


# (vi) Finally create an object of Car and call the method
my_car = Car("Sedan")
my_car.drive()