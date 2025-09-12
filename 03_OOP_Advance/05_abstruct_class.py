# Abstruct Base Class and Abstruct Method.

# -   Abstruct base class is the blue print of the other subclass.
# -   Abstruct base class cannot be instantiated, i.e., the object of the abstruct 
#     class cannot be created.
# -   Abstruct class can only be inherited to other subclasses.
# -   Abstruct method must be overriden in the subclass.
# -   It shares common blue print of the methods in the subclass.

# Implementation in Python

# -   In Python, abstruct base class and abstruct methods are implemented through `abc` module.
# -   In `abc` module, the `ABC` class is used to define abstruct class.
# -   In `abc` module, the `@abstructmethod` decorator is used to define abstruct method.

from abc import ABC, abstractmethod

class DataBaseConnector(ABC):
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

class MySQLConnector(DataBaseConnector):

    def connect(self):
        print(f'\nConnected to MySQL Database...')

    def disconnect(self):
        print(f'Disconnected from MySQL Database.')

    def execute(self, query):
        print(f'Executing MySQL query - {query}')
        return 'Result from MySQL'
    
class ProsgreSQLConnector(DataBaseConnector):

    def connect(self):
        print(f'\nConnected to ProsgreSQL Database...')

    def disconnect(self):
        print(f'Disconnected from ProsgreSQL Database.')

    def execute(self, query):
        print(f'Executing ProsgreSQL query - {query}')
        return 'Result from ProsgreSQL'
    
def run_db_operation(connector):
    connector.connect()
    result = connector.execute('SELECT * FROM user;')
    print(f'Received: {result}')
    connector.disconnect()

if __name__ == '__main__':
    mysql = MySQLConnector()
    postgresql = ProsgreSQLConnector()

    run_db_operation(mysql)
    run_db_operation(postgresql)