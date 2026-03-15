# Class Method: Method that operates on Class itself, not on a specific instance.
# Class method is defined using `@classmethod` decorator. It accepts `cls` as its first
# parameter to reference to class.

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
    
# Creating a regular instance.
date1 = Date(14, 8, 1987)
print(f'Regular Date - {date1.show()}')

# Creating instance with class method.
date2 = Date.from_string('13-03-2020')
print(f'\nDate from string - {date2.show()}')