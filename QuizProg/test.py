# Quiz 1.
print('\nQuiz 1:')
class A:
    def __str__(self):
        return 'a'
    
class B(A):
    def __str__(self):
        return 'b'
    
class C(B):
    pass

o = C()
print(o)

# Quiz 2.
print('\nQuiz 2:')
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
    
for x in I():
    print(x, end='')

# Quiz 3.
print('\nQuiz 3:')

class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.arg = (msg,)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)

# Quiz 4.
print('\nQuiz 4:')
def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')

# Quiz 5.
print('\nQuiz 5:')
class A:
    def __init__(self, v = 1):
        self.v = v

    def set(self, v):
        self.v = v
        return v
    
a = A()
print(a.set(a.v + 1))

# Quiz 6.
print('\nQuiz 6:')
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))

# Quiz 7.
print('\nQuiz 7:')
class A:
    def __str__(self):
        return 'a'
    
class B:
    def __str__(self):
        return 'b'
    
class C(A, B):
    pass

o = C()
print(o)

# Quiz 8.
print('\nQuiz 8:')
class A:
    X = 0
    def __init__(self, v = 0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)
print(c.X)

# Quiz 9.
print('\nQuiz 9:')
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B, A):
    def c(self):
        self.a()

o = C()
o.c()

# Quiz 10.
print('\nQuiz 10:')
class A:
    def __init__(self, v):
        self.__a = v + 1

a = A(0)
# print(a.__a)

# Quiz 11.
print('\nQuiz 11:')
def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o(2)
print(r() + s())

# Quiz 12.
print('\nQuiz 12:')

def f(x):
    try:
        x = x / x
    except:
        print('a', end='')
    else:
        print('b', end='')
    finally:
        print('c', end='')

f(1)
f(0)

# Quiz 13.
print('\nQuiz 13:')

class A:
    pass
class B(A):
    pass
class C(B):
    pass    

print(issubclass(C, A))

# Quiz 14.
print('\nQuiz 14:')

class A:
    v = 2
class B(A):
    v = 1
class C(B):
    pass

o = C()
print(o.v)

# Quiz 15.
print('\nQuiz 15:')
class A:
    A = 1

print(hasattr(A, 'A'))

# Quiz 16.
print('\nQuiz 16:')
def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c

for x in I():
    print(x, end='')

# Quiz 17.
print('\nQuiz 17:')
x = "\\\\"
print(len(x))

# Quiz 18.
print('\nQuiz 18:')
class A:
    A = 1
    def __init__(self):
        self.a = 2

print(hasattr(A, 'a'))

# Quiz 19.
print('\nQuiz 19:')
try:
    raise Exception
except BaseException:
    print('a')
except Exception:
    print('b')
except:
    print('c')

# Quiz 20.
print('\nQuiz 20:')
str1 = 'string'
str2 = str1[:]
print(str1 is str2)

# Quiz 21.
print('\nQuiz 21:')
d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]

for x in d.keys():
    print(d[x][1], end='')

# Quiz 22.
print('\nQuiz 22:')
x = """
"""
print(len(x))

# Quiz 23.
print('\nQuiz 23:')
def fun(x):
    return 1 if x % 2 != 0 else 2

print(fun(fun(1)))

# Quiz 24.
print('\nQuiz 24:')
def fun(d, k ,v):
    d[k] = v

dc = {}
print(fun(dc, '1', 'v'))

# Quiz 25.
print('\nQuiz 25:')
d = {'one': 1, 'three': 3, 'two': 2}
for k in sorted(d.values()):
    print(k, end=' ')

# Quiz 26.
print('\nQuiz 26:')

v = 1 + 1 // 2 + 1 / 2 + 2
print(v)

# Quiz 27.
print('\nQuiz 27:')
z = 2
y = 1
x = y < z or z > y and y > z or z < y
print(x)

# Quiz 28.
print('\nQuiz 28:')
t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)

# Quiz 29.
print('\nQuiz 29:')
def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s

for x in I(3):
    print(x, end='')

# Quiz 30.
print('\nQuiz 30:')
ls = [[c for c in range(r)] for r in range(3)]  

for x in ls:
    if len(x) < 2:
        print('_')

# Quiz 31.
print('\nQuiz 31:')

