'''This script demonstrates various string methods in Python.'''
# Demonstrating the len() function in Python.
print('Demonstrating the len() function in Python.')
print(len('Hello World'))   


# Demonstating the list() function in Python.
print('\nDemonstating the list() function in Python.')
print(list('Taj Mahal'))

# Demonstrating the count() method in Strings.
print('\nDemonstrating the count() method in Strings.')
print('banana'.count('a'))
print('banana'.count('na'))
print('banana'.count('z'))

# Demonstrating the capitalize() method in string.
print('\nDemonstrating the capitalize() method in string.')
print('aBcDEf'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demonstrating the startswith() method
print('\nDemonstrating the startswith() method')
print("omega".startswith("meg"))
print("omega".startswith("om"))

# Demonstrating the endswith() method
print('\nDemonstrating the endswith() method')
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))


# Demonstrating the find() method
print('\nDemonstrating the find() method')
print("Eta".find("ta"))
print("Eta".find("mma"))
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print('kappa'.find('a', 2))

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

print('\nFinding all occurrences of the word "the" in the given text:')
fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

# Demonstrating the isalnum() method
print('\nDemonstrating the isalnum() method')
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print('----')
t = 'Six lambdas'
print(t.isalnum())
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())

t = ' 20E1'
print(t.isalnum())

# Example 1: Demonstrating the isapha() method
print('\nDemonstrating the isapha() method')
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method
print('\nDemonstrating the isdigit() method')
print('2018'.isdigit())
print("Year2019".isdigit())

# Example 1: Demonstrating the islower() method
print('\nDemonstrating the islower() method')
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method
print('\nDemonstrating the isspace() method')
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method
print('\nDemonstrating the isupper() method')
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method
print('\nDemonstrating the join() method')
wonders = ['Great Pyramid of Giza', 'Christ the Redeemer', 'Machu Picchu', 'Chichen Itza', 'Roman Colosseum', 'Taj Mahal']
print(' | '.join(wonders))

# Demonstrating the split() method
print('\nDemonstrating the split() method')
print("phi       chi\npsi".split())
print(".".join("phi       chi\npsi".split()))

# Demonstrating the lower() method
print('\nDemonstrating the lower() method')
print("SiGmA=60".lower())

# Demonstrating the lstrip() method
print('\nDemonstrating the lstrip() method')
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))

# Demonstrating the rstrip() method
print('\nDemonstrating the rstrip() method')   
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
print("python.org".rstrip(".org"))
print("cispo.com".rstrip(".com"))

# Demonstrating the strip() method
print('\nDemonstrating the strip() method')
print("[" + "   aleph   ".strip() + "]")

# Demonstrating the replace() method
print('\nDemonstrating the replace() method')
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demonstrating the rfind() method
print('\nDemonstrating the rfind() method')
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demonstrating the swapcase() method
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method
print("I know that I know nothing. Part 2.".upper())