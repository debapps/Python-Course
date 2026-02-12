# Exception Arguments.

try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end= ' : ')
    print(e.args)

try:
    raise Exception('My Exception Message')
except Exception as e:
    print(e, e.__str__(), sep=' : ', end= ' : ')
    print(e.args)

try:
    raise Exception('My', 'Exception', 'Message')
except Exception as e:
    print(e, e.__str__(), sep=' : ', end= ' : ')
    print(e.args)