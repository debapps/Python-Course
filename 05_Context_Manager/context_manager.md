# Context Manager in Python

-   Context Managers in Python are the powerful tools for managing resources files, DB and Network connections and locks.
-   It ensures that the resources are acquired and released properly, preventing resource leaks.
-   It maintains the code more reliable, readable and maintainable.

## Using `with` statement.

The `with` statement ensures that the resources are properly closed or released in case of exception conditions.

## Creating custom context mananger using classes.

We can create custom context manager to implement the `__enter__()` and `__exit__()` in the class.
