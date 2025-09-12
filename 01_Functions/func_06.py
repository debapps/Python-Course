def add_to_list_bad_practice(item, my_list=[]):
    my_list.append(item)
    return my_list

def add_to_list_good_practice(item, my_list=None):
    if my_list is None:
        my_list = []
    
    my_list.append(item)
    return my_list

print(add_to_list_bad_practice('apple'))
print(add_to_list_bad_practice('banana'))

print(add_to_list_good_practice('apple'))
print(add_to_list_good_practice('banana'))

fruits = []
print(add_to_list_good_practice('apple', fruits))
print(add_to_list_good_practice('kiwi', fruits))