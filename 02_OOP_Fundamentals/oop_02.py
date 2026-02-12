# Class constractor: __init__() method in the class is used to initialize the object.

class Book:
    # `self._title`, `self._author` and `self._price` are the attributes of object instances.
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    # The __str__() method is a special method that defines the string representation 
    # of an object.
    def __str__(self):
        return f"'{self._title}' by {self._author}, priced at Rs. {self._price}"

# Creating Book objects with mandatory attributes: title, author and price.
b1 = Book('The Alchemist', 'Paulo Coelho', 254.00)
b2 = Book('The Kite Runner', 'Hosseini Khaled', 340.00)
b3 = Book('The Book Thief', 'Zusak Markus', 236.00)

print('Accessing attributes directly:')
# We can now access the attributes of each object
print(f"Book 1: '{b1._title}' by {b1._author}, priced at Rs. {b1._price}")
print(f"Book 2: '{b2._title}' by {b2._author}, priced at Rs. {b2._price}")
print(f"Book 3: '{b3._title}' by {b3._author}, priced at Rs. {b3._price}")

print('\nUsing __str__ method:')
# When we print the object, the __str__() method is called to get the string representation of the object.
print('Book 1: ', b1)
print('Book 2: ', b2)
print('Book 3: ', b3)   

print('\nUsing __dict__ attribute:')
# The __dict__ attribute of an object contains a dictionary representation of the 
# object's attributes.
print('Book 1: ', b1.__dict__)
print('Book 2: ', b2.__dict__)
print('Book 3: ', b3.__dict__)

