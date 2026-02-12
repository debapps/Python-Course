# String concatenation and repetition.
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demonstrating the ord() function.

ch1 = 'a' 
ch2 = ' ' # space
ch3 = 'α' # Greek alpha

print(ord(ch1))
print(ord(ch2))
print(ord(ch3))

# Demonstrating the chr() function

print(chr(97))
print(chr(945))
print(chr(ord('x')) == 'x')
print(ord(chr(945)) == 945)

# Demonstrating min() - Example 1
print(min("aAbByYzZ"))

# Demonstrating min() - Examples 2 & 3
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demonstrating max() - Example 1
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))
              