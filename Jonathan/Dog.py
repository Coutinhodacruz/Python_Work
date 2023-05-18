class Dog:
    color = "Black"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        return f"I am {self.name}"

    def make_sound(self):
        return f"{self.name} says Woof Woof"

    def __str__(self):
        return f"I am {self.name}"

    def __repr__(self):
        return f"Dog({self.name}, {self.age})"


tommy = Dog("tommy", " caucasian ")
flip = Dog("flip", "german shepherd")
print(tommy == flip)
print(type(tommy) == type(flip))
print(tommy.color)
print(tommy)
print(repr(tommy))
