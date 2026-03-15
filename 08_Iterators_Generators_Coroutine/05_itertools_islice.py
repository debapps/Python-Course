# Generate first 3 lines from a large file.

import itertools

with open('large_file.txt', 'r') as file:
    large_file_iterable = iter(file)

    file_details = itertools.islice(large_file_iterable, 10, 13)

    for line in file_details:
        print(line.strip())