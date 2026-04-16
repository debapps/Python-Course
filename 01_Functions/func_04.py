# Extended function definition with *args and **kwargs.
# *args – refers to a tuple of all additional, not explicitly expected positional arguments.
# **kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs. 

def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')