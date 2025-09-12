from contextlib import contextmanager

@contextmanager
def file(filename, mode):
    print('Entering Context...')
    f = open(filename, mode)
    yield f
    print('Exiting Context...')
    f.close()

def main():
    with file('test.txt', 'w') as f:
        print('Writing File...')
        f.write('Hello, Dear.. I love you!!')

if __name__ == '__main__':
    main()