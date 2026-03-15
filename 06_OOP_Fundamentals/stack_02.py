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
    
class AdddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self,val)

    def pop(self):
        val = Stack.pop(self)
        if val is not None:
            self.__sum -= val
        return val

    def getSum(self):
        return self.__sum
    
if __name__ == "__main__":
    myStack = AdddingStack()

    for idx in range(5):
        myStack.push(idx)
    
    print('Sum of the Stack Items: ', myStack.getSum())

    for idx in range(5):
        print('Popped Item: ', myStack.pop())