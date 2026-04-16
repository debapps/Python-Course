# Docstring

def calculate_area(length, width):
 """
 Calculates the area of a rectangle.

 Args:
 length (int): The length of the rectangle.
 width (int): The width of the rectangle.

 Returns:
 int: The calculated area of the rectangle.
 """
 # Multiply length and width to find the area
 area = length * width
 return area

# You can access the docstring using the __doc__ attribute
print(calculate_area.__doc__)