# This function calculates the sum of all the digits of a date in yyyymmdd format.

def digit_of_life(dob):
    result = 0
    dob = dob.strip()

    if not dob.isdigit():
        print('Enter date with YYYYMMDD format')
        return 0

    for ch in dob:
        result += int(ch)
        
    if result < 10:
        return result
    else:
        return digit_of_life(str(result))

# Example usage:
date_of_birth = input("Enter your date of birth (YYYYMMDD): ")
life_digit = digit_of_life(date_of_birth)
if life_digit != 0:
    print(f'Your digit of life is: {life_digit}')
    