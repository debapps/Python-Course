# Generators: Generators in Python are special type of functions that allow you to 
# create an iterable sequence of values.

from random import randint

# Generators are created using `yeild` keywords.
def random_number_generator(n):
    for num in range(n):
        yield randint(1, 50)

rand_gen = random_number_generator(5)
print(f'Generator Object Created - {rand_gen}\nType - {type(rand_gen)}')
print('\nRandom numbers')
print(next(rand_gen))
print(next(rand_gen))
print(next(rand_gen))
print(next(rand_gen))
print(next(rand_gen))

try:
    print(next(rand_gen))
except StopIteration as e:
    print(f'{rand_gen} is exhausted. Raised exception {e}')

#  Generator defined with comprehension.
even_num = (num for num in range(11) if num % 2 == 0)
print('\nEven Number:')
for num in even_num:
    print(num)



