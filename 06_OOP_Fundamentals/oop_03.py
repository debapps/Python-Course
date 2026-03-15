# Instance Methods and attributes.

class Book:
    # `self.title`, `self.author` and `self.price` are the attributes of object instances.
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Instance methods.
    def get_details(self):
        return f'{self.title} by {self.author}'
    
    def apply_discount(self, discount_percentage):
        discount = self.price * discount_percentage / 100
        self.discounted_price = self.price - discount
        return self.discounted_price

# Creating Book objects with mandatory attributes: title, author and price.
b1 = Book('The Alchemist', 'Paulo Coelho', 254.00)
b2 = Book('The Kite Runner', 'Hosseini Khaled', 340.00)
b3 = Book('The Book Thief', 'Zusak Markus', 236.00)

# Call the instance method to get details of each book object.
print(f'Book 1: {b1.get_details()}')
print(f'Book 2: {b2.get_details()}')
print(f'Book 3: {b3.get_details()}')

# Apply discount of 20% on book 2.
print(f'20% Discounted price of "{b2.get_details()}" is Rs. {b2.apply_discount(20):.2f}')

