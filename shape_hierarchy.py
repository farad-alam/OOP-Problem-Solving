class Shape:
    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length    
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

l1 = Rectangle(10, 20)
l2 = Circle(5)

print(l1.area())
print(l2.area())