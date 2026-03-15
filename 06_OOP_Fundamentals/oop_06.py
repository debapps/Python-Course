# Class and Object Properties: Attributes.

class Classy:
    varia = 1
    def __init__(self, name):
        self.name = name


print(Classy.__dict__)
obj = Classy('Debaditya')
print(obj.__dict__)

class Classy:
    varia = 1
    def __init__(self, val):
        Classy.varia = val

print(Classy.__dict__)
obj = Classy(10)
print(Classy.__dict__)
print(obj.__dict__)