from Dog import Dog


class Pugs(Dog):
    def make_sound(self, sounds="Woof Woof"):
        return f"{self.name} says {sounds}"





cyn = Pugs("Cynthia", 2)
print(cyn.make_sound())
print(isinstance(cyn, Dog))
print(isinstance("1", str))
