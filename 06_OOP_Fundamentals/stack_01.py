class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        if self.isEmpty():
            return None
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val
    
    def isEmpty(self):
        return len(self.__stackList) == 0
    
if __name__ == "__main__":
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    print(myStack.pop())  # Output: 3
    print(myStack.pop())  # Output: 2
    print(myStack.isEmpty())  # Output: False
    print(myStack.pop())  # Output: 1
    print(myStack.isEmpty())  # Output: True    