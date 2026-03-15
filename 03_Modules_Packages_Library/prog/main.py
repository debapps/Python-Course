from sys import path
import os

# Get the parent directory.
parent_dir = os.path.dirname(os.getcwd())

# Append the module path to sys.path
module_path = os.path.join(parent_dir, 'modules')
path.append(module_path)

from module import sum_list, prod_list


list1 = [elem for elem in range(10)]
list2 = [elem for elem in range(1, 10)]
print(f'Sum of {list1} is {sum_list(list1)}')
print(f'Product of {list2} is {prod_list(list2)}')

