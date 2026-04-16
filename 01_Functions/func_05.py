# forwarding arguments to other functions.
def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs)
    
    # If you remove the * and **, the function will receive the arguments 
    # as a tuple and a dictionary, respectively, 
    # instead of unpacking them into individual arguments. 
    
    # super_combiner(args, kwargs)

def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')