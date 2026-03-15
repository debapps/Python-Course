# itertools modules can have a number of useful, memory efficient iterators.
# The infinite iterators never stops.

import itertools

# count iterators.
print('\ncount iterator.')
# counter = itertools.count()
counter = itertools.count(start=5, step=2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

print('\nCreating sequence data.')
data = ['Alice', 'Bob', 'Charlie', 'David']
sequence_data = zip(itertools.count(start=1), data)

for item in sequence_data:
    print(item)

# cycle iterator.
print('\ncycle iterator')
result = itertools.cycle('ABCD')

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# repeat iterator.
print('\nrepeat iterator.')
result = itertools.repeat(2)

print(next(result))
print(next(result))
print(next(result))

print('\nGenerating Cube of numbers from 1 to 10.')
cubes = map(pow, range(1, 11), itertools.repeat(3))
print(list(cubes))
