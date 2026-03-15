'''The function able to input integer values and to 
   check if they are within a specified range.'''

def readint(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            assert min <= value <= max
            return value
        except ValueError:
            print('Error: wrong input')
        except AssertionError:
            print(f'Error: the value is not within permitted range ({min}..{max})')

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)