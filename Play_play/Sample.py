class Sample:
    def __init__(self, color=" green ", filled=True):
        self.__color = color
        self.__filed = filled


    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color


    def isFilled(self):
        return self.__filed

    def setFilled(self, filled):
        self.__filed = filled

    def __str__(self):
        return " color " + self.__color + \
            " and filled: " + str(self.__filed)
