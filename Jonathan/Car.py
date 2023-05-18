class Car:

    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

    def __str__(self):
        return f"The {self.color} car has {self.milage:,} miles.\n"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError("Invalid Type")


    @color.deleter
    def color(self):
        raise AttributeError("Attribute cannot be deleted")


    # def drive(self, number):
    #     self.milage += number
        # return f"The {self.color} car has {self.milage:,} miles"


# toyota = Car("Black",0)
# toyota.drive(100)
# print(toyota.milage)
benz = Car("Camry", 20000)
# volvo = Car("Red",30000)
print(benz.color)
benz.color = "blue"
print(benz.color)
# print(volvo)
