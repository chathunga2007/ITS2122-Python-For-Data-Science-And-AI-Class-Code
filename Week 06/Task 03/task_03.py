class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


employee1 = Employee("Chathunga", 18)
employee1.show_details()