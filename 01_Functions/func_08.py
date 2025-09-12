# Higher Order Functions: A function that meets one or both of the following criteria.
# - Takes a function as an argument.
# - Returns a function as it result.

# A function that takes another function as an argument.
def apply_ops(items, op_func):
    '''A higher order function that apply op_func to each element of items.'''
    results = [op_func(item) for item in items]
    return results

def add_one(x):
    '''Adds one to its parameter x.'''
    return x + 1

numbers = [2, 5, 6, 4, 1]
added_numbers = apply_ops(numbers, add_one)
print(f'\nNumbers applying add one: {added_numbers}')

def make_upper(name):
    '''Returns the upper-case.'''
    return name.upper()

names = ['bittu', 'anurag', 'anuradha', 'montu', 'rumpa']
print(f'\nNames in upper-case: {apply_ops(names, make_upper)}')

# A function that returns another function.
def multiplier(n):
    '''This function returns a functions that multiply n with its parameter.'''

    def times(x):
        return x * n
    
    return times

five_times = multiplier(5)
print(f'\nThe 5 times of 15 is: {five_times(15)}')

three_times = multiplier(3)
print(f'\nThe 3 times of 20 is: {three_times(20)}')

    

