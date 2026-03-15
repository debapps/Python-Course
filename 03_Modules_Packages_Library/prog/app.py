from sys import path
import os

# Get the parent directory.
parent_dir = os.path.dirname(os.getcwd())
# Append the parent directory to sys.path
path.append(parent_dir)

from mylib.packageA import moduleB
from mylib.packageA.moduleA import function_1, function_2
from mylib.moduleE import function_5, function_6

print('In the App')
print(function_1())
print(function_2())

print(moduleB.function_3())
print(moduleB.function_4()) 

print(function_5())
print(function_6())

from mylib.packageB.subpackB.moduleD import function_5 as function_d5
print(function_d5())

print('End of App')