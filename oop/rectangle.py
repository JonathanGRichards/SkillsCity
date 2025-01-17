class Rectangle:
    def __init__(self, width = 5, height = 15):
        self.__width = width
        self.__height = height

    # Getter methods
    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    # Setter methods
    def set_width(self, width):
    if (type(width) == 'int'):
        self._width = width
    else:
        print('error')

    def set_height(self, height):
        self._height = height

    # Method to calculate area
    def calculate_area(self):
        return self._width * self._height

rectangle = Rectangle()

print(rectangle.get_height())