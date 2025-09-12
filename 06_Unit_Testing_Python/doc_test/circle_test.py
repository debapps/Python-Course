from math import pi
# Define the class 'Circle' and its methods with proper doctests:
class Circle:

    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.radius
        2.5

        >>> c2 = Circle(-7)
        Traceback (most recent call last):
        ValueError: Radius must be a positive number.

        >>> c2 = Circle('two')
        Traceback (most recent call last):
        TypeError: Radius must be a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be a number.')
        
        if radius < 0:
            raise ValueError('Radius must be a positive number.')
            
        self.radius = radius
        
    def area(self):
        # Define doctests for area method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.area()
        19.63
        """
        # Define area functionality:
        return round(pi * pow(self.radius, 2), 2)
        
    def circumference(self):
        # Define doctests for circumference method:
        """
        >>> c1 = Circle(2.5)
        >>> c1.circumference()
        15.71
        """
        # Define circumference functionality:
        return round(2 * pi * self.radius, 2)