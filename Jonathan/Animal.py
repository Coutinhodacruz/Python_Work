class Animal:


    def __init__(self,name,color,sounds,age,type):
        self.name = name
        self.color = color
        self.sounds = sounds
        self.age = age
        self.type = type

    def sounds(self):
        return f"{self.name}"

    def __str__(self):
        return f"I am {self.name} says bleat"
