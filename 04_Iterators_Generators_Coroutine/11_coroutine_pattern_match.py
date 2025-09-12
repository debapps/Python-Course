# This program uses a Coroutine to find error in application log file using pattern matching.

# Coroutine Decorator.
def couroutines(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c
    
    return wrapper

@couroutines
def text_pattern(pattern):
    try:
        while True:
            text = yield
            if pattern in text:
                print(f'{pattern} Match Found - {text}')
    except GeneratorExit:
        print('Coroutine Closed.')

if __name__ == '__main__':
    print('\n-------- Find ERROR using Coroutine --------')

    searcher = text_pattern('ERROR')

    with open('app.log', 'r') as log_file:
        for line in log_file:
            searcher.send(line.strip())

    searcher.close()