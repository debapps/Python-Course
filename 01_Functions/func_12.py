# Decorator Function: takes another function as an argument, adds some functionality, 
# and returns another function. 

import time

def timer_decoratior(func):
    def timer_wrapper(*args, **kwargs):
        start_time = time.time()
        print(f'\nProcessing start at: {start_time}')
        func(*args, **kwargs)
        end_time = time.time()
        print(f'\nProcessing start at: {end_time}')
        print(f'Time taken: {round(end_time - start_time, 4)}\n')

    return timer_wrapper

@timer_decoratior
def delay_processing(n):
    '''This Function introduce some delay.'''
    for _ in range(n):
        sum([idx*idx for idx in range(100000)])

    

delay_processing(10)