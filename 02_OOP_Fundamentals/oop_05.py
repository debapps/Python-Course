# Static Method: Static method is utility function those are logically grouped into a class,
# but does not need to have access to instance's attributes or state. 
# It doesn't take `self` or `cls` as an argument. `@staticmethod` decorator is used to define 
# the static method.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Instance Method.
    def show(self):
        return f'{self.day}/{self.month}/{self.year}'
    
    # Class Method.
    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)
    
    # Static Method.
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
# Creating a regular instance.
date1 = Date(14, 8, 1987)
print(f'Regular Date - {date1.show()}')

# Creating instance with class method.
date2 = Date.from_string('13-03-2020')
print(f'\nDate from string - {date2.show()}\n')

# We can call the static method directly from the class
# without creating an instance.
print(f"Is 2024 a leap year? {Date.is_leap_year(2024)}")
print(f"Is 2023 a leap year? {Date.is_leap_year(2023)}")