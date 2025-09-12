# map(), filter(), reduce() functions: Higher order function examples.

import random
from functools import reduce

# Get the initial list of 10 numbers.
numbers = [random.randint(1, 50) for _ in range(10)]
print(f'Initial list of numbers: {numbers}')

# The map() function: maps each elements in the list to a function.
square_numbers = list(map(lambda x: pow(x, 2), numbers))
print(f'Squared numbers list: {square_numbers}')

# The filter() function: filters elements based on some condition.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f'List of even numbers: {even_numbers}')

# The reduce() function: reduces elements of a list into a single value 
# based on the function argument.
numbers_total = reduce(lambda x, y: x + y, numbers)
print(f'The sum of the numbers: {numbers_total}')

min_number = reduce(lambda x, y: x if (x < y) else y, numbers)
print(f'The smallest number: {min_number}')
