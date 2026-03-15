# Custom Iterators can be created by implementing the __iter__() and __next__() methods in a class.

# This program will create a custom iterators that takes a list of numbers and 
# returns even number iteration.

class EvenNumberList:
    def __init__(self, numbers):
        print('__init__')
        self._numbers = numbers
        self._idx = 0

    def __iter__(self):
        print('__iter__')
        return self
    
    def __next__(self):
        print('__next__')
        while self._idx < len(self._numbers):
            current_num = self._numbers[self._idx]
            self._idx += 1
        
            if current_num % 2 == 0:
                return current_num

        raise StopIteration

def main():
    num_list = [num for num in range(1, 11)]
    even_numbers = EvenNumberList(num_list)

    print('\nEven Number List:')
    for num in even_numbers:
        print(num)

if __name__ == '__main__':
    main()