# This program calculates the sum of the prime numbers from 1 to 100.

from functools import reduce

numbers = [num for num in range(1, 101)]

def prime(n):
    '''Returns True if the number is prime.'''
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

prime_numbers = list(filter(prime, numbers))
sum_of_prime_numbers = reduce(lambda x, y: x + y, prime_numbers)
print(f'The sum of prime numbers from 1 to 100: {sum_of_prime_numbers}')
