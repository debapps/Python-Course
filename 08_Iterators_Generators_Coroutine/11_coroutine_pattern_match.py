# This program uses a Coroutine to find error in application log file using pattern matching.

# Coroutine Decorator.
def coroutines(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c
    
    return wrapper

@coroutines
def text_pattern(pattern):
    try:
        while True:
            text = yield
            if pattern in text:
                print(f'{pattern} Match Found - {text}')
    except GeneratorExit:
        print(f'{pattern} Seracher Coroutine Closed.')

if __name__ == '__main__':
    print('\n-------- Find ERROR using Coroutine --------')

    error_srch = text_pattern('ERROR')
    debug_srch = text_pattern('DEBUG')

    with open('app.log', 'r') as log_file:
        for line in log_file:
            error_srch.send(line.strip())
            debug_srch.send(line.strip())

    error_srch.close()
    debug_srch.close()