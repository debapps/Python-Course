# Class constractor: __init__() method in the class is used to initialize the object.

class Book:
    # `self.title`, `self.author` and `self.price` are the attributes of object instances.
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

# Creating Book objects with mandatory attributes: title, author and price.
b1 = Book('The Alchemist', 'Paulo Coelho', 254.00)
b2 = Book('The Kite Runner', 'Hosseini Khaled', 340.00)
b3 = Book('The Book Thief', 'Zusak Markus', 236.00)

# We can now access the attributes of each object
print(f"Book 1: '{b1.title}' by {b1.author}, priced at Rs. {b1.price}")
print(f"Book 2: '{b2.title}' by {b2.author}, priced at Rs. {b2.price}")
print(f"Book 3: '{b3.title}' by {b3.author}, priced at Rs. {b3.price}")