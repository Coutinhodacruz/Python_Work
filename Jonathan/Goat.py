from Animal import Animal


class Goat(Animal):
    def sounds(self, sounds="bleat"):
        return f"{self.name} says {sounds}"


vee = Animal("goat", "black", "bleat,", 2, "male")
print(vee)
print(isinstance(vee,Animal))
