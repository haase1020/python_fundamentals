# import importlib
# importlib.reload(cars)

class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):  # gets called under the hood when create new instance of class
        print("new car!")
        self.name = name

    def __str__(self):
        return f"My car the {self.name} currently {self.runs}"

    def __repr___(self):
        return f"car({self.name})"

    # self shows it's an instance method. ALl instance methods within class take self as 1st arg.
    def start(self):
        if self.runs:
            print("Car is started. Vroom vroom!")
        else:
            print("Car is broken :(")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.get_number_of_wheels


my_car = Car("Subaru")
print(my_car.start())
print(type(my_car))
print(isinstance(my_car, int))
print(str(my_car))
print(repr(my_car))
