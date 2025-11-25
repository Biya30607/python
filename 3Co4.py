class Rectangle:
    def __init__(self, length, width):
        self.__length = length 
        self.__width = width    

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)

print("Rectangle 1 area:", rect1.area())
print("Rectangle 2 area:", rect2.area())

if rect1 < rect2:
    print("Rectangle 1 has smaller area than Rectangle 2")
else:
    print("Rectangle 1 has larger or equal area than Rectangle 2")
