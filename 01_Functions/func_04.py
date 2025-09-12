# This program demonstates the local and global scopes.

# This is a global variable
global_message = "I am a global message."

def demonstrate_scope():
 # This is a local variable
 local_message = "I am a local message."
 print(f"Inside the function: {local_message}")
 print(f"Inside the function: {global_message}")

demonstrate_scope()

# This will work because global_message is in the global scope
print(f"Outside the function: {global_message}")

# This will cause an error because local_message is not in the global scope
try:
 print(f"Outside the function: {local_message}")
except NameError as e:
 print(f"\nCaught an error: {e}")