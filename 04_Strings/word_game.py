def find_word(first, second):
    '''
    Docstring for find_word:

    This function takes two words as input: one being a word and the second being a 
    combination of any characters. The function checkes if the characters comprising the first string 
    hidden inside the second string?
    
    :param first: A meaningful word
    :param second: A string of random characters.
    '''
    first = first.lower()
    second = second.lower()
    first_len = len(first)
    second_len = len(second)    
    idy = 0

    search_list = ['*' for _ in range(second_len)]

    for idx in range(first_len):
        char = first[idx]
        found_idx = second.find(char, idy)
        if found_idx != -1:
            search_list[found_idx] = char
            idy = found_idx + 1
        else:
            return 'No'

    result = ''.join(search_list).replace('*', '')
    if result == first:
        return 'Yes'
    else:
        return 'No'

# Example usage:
if __name__ == "__main__":
    print(find_word("dog", "vcxzxduybfdsobywuefgas"))  
    print(find_word("dog", "vcxzxdcybfdstbywuefsas"))   
    print(find_word("donor", "Nabucodonosor")) 
    print(find_word("donut", "Nabucodonosor")) 