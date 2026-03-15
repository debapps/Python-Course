# Lambda Function: Anonymous Functions with one return expression.
# Lambda functions are also known as anonymous functions because they do not have a name. 
# They are defined using the lambda keyword and can take any number of arguments but 
# can only have one expression. 
# The expression is evaluated and returned when the function is called.
# lambda parameters : expression

# Lambda function to add two numbers.
add = lambda x, y: x + y

print(f'The sum of 10 and 23 is: {add(10, 23)}')

# Lambda functions are often used as an argument to other functions.
students = [('Anuradha', 55), ('Susmita', 34), ('Tania', 23)]

# Sort the students based on id.
sorted_students = sorted(students, key=lambda students: students[1])

print(f'Student List: {students}')
print(f'Sorted Student List: {sorted_students}')