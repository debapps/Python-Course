# The groupby function returns an iterator that contains consecutive keys and groups.
# The key must be sorted.

# This program reads a JSON file and groups the data based on state.
import json
import itertools

with open('person.json', 'r') as person_file:
    data = json.load(person_file)

# Sort the data using State.
state_key = lambda person: person['state']
person_data = sorted(data, key=state_key)

# Get the person group.
person_group = itertools.groupby(person_data, state_key)

for state, group in person_group:
    person_list = list(group)
    print(f'State - {state}\tNumber of person - {len(person_list)}')
    
    for person in person_list:
        print(person)

    print()