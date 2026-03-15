# User defined Exceptions. 

class PizzaError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, pizza, message):
        super().__init__(message)
        self.pizza = pizza

class TooMuchCheeseError(PizzaError): 
    """Raised when the pizza has too much cheese."""
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza, message)
        self.cheese = cheese

def make_pizza(pizza, cheese):
    acceptable_cheese = 100
    available_pizza = ['Margherita', 'Pepperoni', 'Hawaiian']

    if pizza not in available_pizza:
        raise PizzaError(pizza, f"Invalid pizza type: {pizza}")

    if cheese > acceptable_cheese:
        raise TooMuchCheeseError(pizza, cheese, f"Too much cheese: {cheese}g exceeds the limit of {acceptable_cheese}g")

    print(f"Making a {pizza} pizza with {cheese}g of cheese.")

# Example usage:
if __name__ == "__main__":
    pizza_orders = [('Pepperoni', 120), ('Veggie', 80), ('Margherita', 90)]

   
    for pizza, cheese in pizza_orders:
        try:
            make_pizza(pizza, cheese)
        except TooMuchCheeseError as e: 
            print(f"Error: {e}") 
        except PizzaError as e: 
            print(f"Error: {e}")        