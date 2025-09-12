# Polymorphism: It means "many forms". It allows objects of different classes to be 
# treated as objects of a common superclass. It means a single function or method name can 
# have different implementations depending on the object it's called on.

# Method overriding is the primary mechanism for achieving polymorphism in Python. 
# It's when a subclass provides a specific implementation of a method 
# that is already defined in its parent class. 
# When you call the method on an object of the subclass, 
# Python executes the subclass's version instead of the parent class's version.

from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def area(self):
        raise NotImplementedError('The child class has to implement the method.')
    
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2)
    
def calculate_area(shape):
    print(f'\nArea of the {shape.get_name()}: {shape.area():.2f}')

if __name__ == '__main__':
    r = Rectangle('Rectangle', 20, 5)
    c = Circle('Circle', 7)


    calculate_area(r)
    calculate_area(c)