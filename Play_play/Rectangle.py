from Sample import Sample


class Rectangle(Sample):
    def __init__(self, width=1, height=1):
        super().__init__()
        self.__width = width
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
