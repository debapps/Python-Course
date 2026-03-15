# Reading and Filtering a Log File using Generator.
import datetime
import time

# Create a sample application log file.
# print('\n----------- Generating Log file ------------------')
# with open('app.log', 'w') as log_file:
#     log_file.write(f'{datetime.datetime.now()} -- INFO: Application Started.\n')
#     log_file.write(f'{datetime.datetime.now()} -- DEBUG: User "Alice" logged in.\n')
#     time.sleep(1)
#     log_file.write(f'{datetime.datetime.now()} -- DEBUG: User "Charles" logged in.\n')
#     log_file.write(f'{datetime.datetime.now()} -- ERROR: Database connection failed.\n')
#     time.sleep(1)
#     log_file.write(f'{datetime.datetime.now()} -- INFO: Remote API Called.\n')
#     log_file.write(f'{datetime.datetime.now()} -- INFO: Processing Data.\n')
#     time.sleep(2)
#     log_file.write(f'{datetime.datetime.now()} -- INFO: Remote API Returned.\n')
#     log_file.write(f'{datetime.datetime.now()} -- ERROR: API Auth failure.\n')
# print('\n----------- Log file generated ------------------')

# Generator Function.
def filter_error(path):
    '''A generator function that filter the errors in the log file.'''

    with open(path, 'r') as log_file:
        for line in log_file:
            if 'ERROR' in line:
                yield line.strip()

print('\n----------- ERRORS from log file ------------------')
# error_generator = filter_error('app.log')

# Generator Expression.
error_generator = (line.strip() for line in open('app.log', 'r') if 'ERROR' in line)

for error in error_generator:
    print(f'Error Found: {error}')