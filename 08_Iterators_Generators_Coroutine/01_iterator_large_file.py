# An iterable is a object that can be looped over, i.e., list, tuple etc.
# An iterator is a object that manage the state of iteration.
# An iterable object has __iter__() method, that returns the iterator object.
# An iterator object has __next__() method, that returns the next item in the sequence. 
# When there is no more item, __next__() method raises StopIteration exception.
# Python loop automates the iteration process. It calls iter() method to get the iterator and 
# repeatedly calls next() method until StopIteration exception occurs.

# This program create a file and iterates it content line by line 
# using manual way and then by python loop.

content = [
    'Line 1: The purpose of our lives is to be happy - Dalai Lama',
    'Line 2: Life is what happens when you\'re busy making other plans - John Lennon',
    'Line 3: The best and most beautiful things in the world cannot be seen or even touched—they must be felt with the heart - Helen Keller',
    'Line 4: Happiness is not something ready-made. It comes from your own actions - Dalai Lama',
    'Line 5: The greatest happiness you can have is knowing that you do not need any - William Saroyan',
    'Line 6: Relationships are like a dance, with a little give and take, and a lot of trust - Unknown',
    'Line 7: A great relationship is about two things: First, appreciating the similarities, and second, respecting the differences - Unknown',
    'Line 8: Love is a two-way street constantly under construction - Carroll Bryant',
    'Line 9: Don\'t walk in front of me… I may not follow. Don\'t walk behind me… I may not lead. Walk beside me… and just be my friend - Albert Camus',
    'Line 10: The real test of a relationship is how you handle disagreements - Unknown',
]

# Create and write the text file.
with open('quotes.txt', 'w') as file:
    for line in content:
        file.write(f'{line}\n')

# Reading the file in manual way.
print('\n--- Manual iteration using iter() and next() ---\n')
with open('quotes.txt', 'r') as file:
    file_iterator = iter(file) # Generate the Iterator.

    while True:
        try:
            print(next(file_iterator).strip())
        except StopIteration as e:
            print('\nEnd of file reached.')
            break

# Reading file using for loop.
print('\n--- Automatic iteration using python for loop ---\n')
with open('quotes.txt', 'r') as file:
    for line in file:
        print(line.strip())