# This program generates Fibbonacci Series using Generators.

def fibbonacci_generator(n):
    x1, x2 = 0, 1
    count = 0

    while count < n:
        yield x1
        x1, x2 = x2, x1 + x2
        count += 1

    
def main():
    print('\nFibbonacci Series.')
    n = int(input('Enter the series length - '))
    
    for fib in fibbonacci_generator(n):
        print(fib, end=' ')

if __name__ == '__main__':
    main()