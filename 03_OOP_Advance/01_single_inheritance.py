# Single Inheritance: A class inherits attributes and methods from single base/parent class.

# A company has base class: Employee. Different job roles like Developer, Manager classes
# inherits attributes and methods from single base class Employee.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f'\nName: {self.name}, Salary: ${self.salary}')

    def give_raise(self, percent):
        self.salary += self.salary * percent / 100
        print(f'New Salary for {self.name}: {self.salary}')

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print(f'{self.name} is writing code in {self.programming_language}')

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.reportees = []

    def add_reportee(self, employee):
        self.reportees.append(employee)
        print(f'{employee.name} is added to {self.name}\'s team.')

    def conduct_meeting(self):
        print(f'{self.name} is conducting meetings for {self.department} department.')


if __name__ == '__main__':
    d1 = Developer('Anuradha', 5000, 'Kotlin')
    d2 = Developer('Tania', 3000, 'Cobol')
    m1 = Manager('Bittu', 8000, 'IT')

    d1.show_info()
    d1.write_code()

    d2.show_info()
    d2.write_code()

    m1.show_info()
    m1.add_reportee(d1)
    m1.add_reportee(d2)
    m1.conduct_meeting()

    d2.give_raise(10)
    