# The key benefit of Generators is "lazy evaluation". 
# The values are produced on the fly, instead of storing the entire collection into the memory.

from sys import getsizeof

data_size = 1_000_000

# Conventional memory intensive approach using list.
print('\n-------- Using List Comprehension --------')
large_data = [item for item in range(data_size)]

print(f'Size of data in memory (bytes): {getsizeof(large_data)}')
print(f'The first five elements: {large_data[:5]}')
del large_data

# Using memory efficient generator approach.
print('\n-------- Using Generator Expression --------')
large_generator = (item for item in range(data_size))

print(f'Size of data in memory (bytes): {getsizeof(large_generator)}')
print(f'The first five elements:')
for _ in range(5):
    print(next(large_generator), end=', ')
