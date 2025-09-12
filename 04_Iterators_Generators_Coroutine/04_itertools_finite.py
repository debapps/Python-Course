# Finite iterators using itertools.

import itertools
# Chaining Iterables: This function takes several iterables and treats them as a 
# single, continuous sequence.

print(f'\nChaining Iterables.')

# Product sales data.
wb_sales = [200, 432, 543, 656]
bihar_sales = [987, 234, 432]
up_sales = [34, 231]

all_sales = itertools.chain(wb_sales, bihar_sales, up_sales)
total = 0

for sales in all_sales:
    total += sales
    print(f'Processing Sales Rs. {sales}')

print(f'\nTotal Sales: Rs. {total}')

# Generating Combinations: This function generates all possible unordered combinations of 
# a specific length from an iterable.

print('\nCreating all possible two-person teams from a list of candidates for a project.')
candidates = ['Alice', 'Bob', 'Charlie', 'David']

# Generate all possible teams of 2
all_teams = itertools.combinations(candidates, 2)

print("All possible 2-person teams:")
for team in all_teams:
    print(team)

# Generating Permutations.
digit_list = list(range(1, 5))
all_permutations = itertools.permutations(digit_list, 3)

print(f'\n\nGenerating all possible permutations of {digit_list} to fill 4 places.')
for item in all_permutations:
    print(item, end=' ')

print()

# Slicing a iterator.
print('\nSlicing a iterator using islice() starting from 5 to 20 by step 2.')
print(list(itertools.islice(itertools.count(start=1), 5, 20, 2)))