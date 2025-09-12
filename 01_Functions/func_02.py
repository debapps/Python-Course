# Positional Argument, Keyword Argument and Default Parameter.

# A Function with positional, and default parameters.
def describe_pet(pet_name, pet_type='dog'):
    print(f'I have a lovely {pet_type}.\nIts name is {pet_name}.\n\n')

# Function calling with positional arguments.
print('Calling with positional arguments.')
describe_pet('harry', 'hamster')

# Function calling with keyword arguments.
print('Calling with keyword arguments.')
describe_pet(pet_name='Newton', pet_type='cat')

# Function calling using default argument.
print('Calling using default argument.')
describe_pet('Tupu')