class Car:
    # (i) Class attribute shared by all instances
    wheels = 4

    # (ii) Instance method drives_to (or drive_to)
    def drives_to(self, destination):
        print(f"The car is driving to {destination} using {self.wheels} wheels.")

    # (iii) Instance method show_wheel_count
    def show_wheel_count(self):
        print(f"Total wheels: {Car.wheels}")


# Example usage:
my_car = Car()

# Test requirement (ii)
my_car.drives_to("Colombo")

# Test requirement (iii)
my_car.show_wheel_count()