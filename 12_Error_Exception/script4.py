def reciprocal(n):
    try:
        result = 1 / n
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: input must be a number.")
        return None
    # `else` block in exception handling is executed 
    # if no exceptions are raised in the `try` block. 
    # It is useful for code that should only run if the `try` block succeeds without errors.
    else:
        return result
    # `finally` block is executed regardless of whether an exception was raised or not.
    # It is typically used for cleanup actions that must be performed under all circumstances, 
    # such as closing files or releasing resources.
    finally:
        print("Execution of the reciprocal function is complete.")
    
print(reciprocal(5)) # Should return 0.2
print(reciprocal(0))  # Should print an error message about division by zero
print(reciprocal("a"))  # Should print an error message about input type