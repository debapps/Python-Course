#! /usr/bin/env python3

'''module.py - An example of a Python module.'''

__counter = 0

def sum_list(lst):
    '''This function returns the sum of the elemement of a list of numbers.'''

    global __counter
    __counter += 1

    sum = 0
    for elem in lst:
        sum += elem

    return sum

def prod_list(lst):
    '''This function returns the product of the elements of a list of numbers.'''

    global __counter
    __counter += 1

    prod = 1
    for elem in lst:
        prod *= elem

    return prod

if __name__ == '__main__':
    print('Testing the module functions:')
    list1 = [elem for elem in range(10)]
    list2 = [elem for elem in range(1, 10)]
    print(f'Sum of {list1} is {sum_list(list1)}')
    print(f'Product of {list2} is {prod_list(list2)}')
