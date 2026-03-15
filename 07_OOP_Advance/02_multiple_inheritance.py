# Multiple Inheritance: A class inherits attributes and methods 
# from multiple base/parent classes.

# A Smartphone is a device that has the capabilities of both a traditional phone for calling 
# and a computer for running applications.

class Phone:
    def make_calls(self, number):
        print(f'Calling to {number} ...')

    def send_message(self, number, message):
        print(f'Message send to {number}: \n{message}')

class Computer:
    def run_application(self, app):
        print(f'Running Application - {app}')

    def connect_wifi(self):
        print(f'Connected to Wi-Fi.')

class SmartPhone(Phone, Computer):
    def __init__(self, brand, model):
       self.brand = brand
       self.model = model

    def show(self):
        print(f'\nSmartphone Brand: {self.brand} Model: {self.model}')

    
if __name__ == '__main__':
    my_smartphone = SmartPhone('Iphone', '13 Pro')

    my_smartphone.show()
    my_smartphone.connect_wifi()
    my_smartphone.run_application('YouTube')
    my_smartphone.make_calls('913-003-8722')
    my_smartphone.send_message('612-987-2345', 'I love you!')