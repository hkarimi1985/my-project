class Employee:
    ''' Defining an employee'''

    num_of_employees = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        num_of_employees += 1

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @property
    def email(self):
        return self.first+'.'+self.last+'@hk.ai'

    @classmethod
    def from_string(cls, emp_str):
        first, last = emp_str.split(' ')
        return cls(first,last)


class Developer(Employee):

    def __init__(self, first, last, salary):
        Employee.__init__(self, first, last)
        self.salary = salary

    @classmethod
    def from_string(cls, dev_str):
        name, salary = dev_str.split(',')
        salary = int(salary)
        first, last = name.split(' ')
        return cls(first, last, salary)
