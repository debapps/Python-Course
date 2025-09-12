# We can write coroutine decorator to create coroutines.

# Coroutine Decorator.
def couroutines(func):
    def wrapper(*args, **kwargs):
        c = func(*args, **kwargs)
        next(c)
        return c
    
    return wrapper

# The coroutine generates token numbers for input data.

@couroutines
def token_issuer(token_id = 0):
    try:
        while True:
            name = yield
            token_id += 1
            print(f'Token number for {name}: {token_id}')
    except GeneratorExit:
        print('Token issuer exit.')

if __name__ == '__main__':
    token = token_issuer(100)

    token.send('Debaditya')
    token.send('Anuradha')
    token.send('Anurag')
    token.send('Tania')

    # close the coroutine.
    token.close()