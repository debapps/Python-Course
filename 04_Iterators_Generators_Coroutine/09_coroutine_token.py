# Coroutines: Special types of generator that receives value on the fly and process it and wait
# for new data.

# 1. We can trigger coroutine processing by next(). The 'yeild' inside the 
# coroutine receives the value.
# 2. We can send new data by coroutine.send(value).
# 3. we can close corouting processing by calling close() method.

# The coroutine generates token numbers for input data.

def token_issuer(token_id = 0):
    try:
        while True:
            name = yield
            token_id += 1
            print(f'Token number for {name}: {token_id}')
    except GeneratorExit:
        print('Token issuer exit.')

if __name__ == '__main__':
    token = token_issuer()
    
    # Starts the coroutine.
    next(token)

    token.send('Debaditya')
    token.send('Anuradha')
    token.send('Anurag')
    token.send('Tania')

    # close the coroutine.
    token.close()