import logging
import time
#
# logging.basicConfig(filename="example.log", level=logging.DEBUG,
#                             format='%(asctime)s: %(name)s: %(filename)s: %(message)s')
logger = logging.getLogger('Employee')
formatter = logging.Formatter('%(created)s: %(name)s: %(filename)s: %(message)s')
f_handler = logging.FileHandler(filename='sample.log')
logger.setLevel(logging.DEBUG)
f_handler.setFormatter(formatter)
logger.addHandler(f_handler)


def LoggerDecorator(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        logger.info('running function \"{}\" , run_time = {}ms'.format(orig_func.__name__, t2*1000))
        return result
    return wrapper


class Employee:
    ''' Defining an employee'''

    num_of_employees = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        Employee.num_of_employees += 1

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @property
    def email(self):
        return self.first+'.'+self.last+'@hk.ai'

    @classmethod
    @LoggerDecorator
    def from_string(cls, emp_str):
        first, last = emp_str.split(' ')
        return cls(first, last)

    def __str__(self):
        return 'Employee: {} {}'.format(self.first, self.last)

    @classmethod
    @LoggerDecorator
    def get_num_of_employee(cls):
        print('Number of employees = {}'.format(cls.num_of_employees))


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

    def __str__(self):
        msg = super().__str__() + ', salary={}'.format(self.salary)
        return msg


class Manager(Employee):

    def __init__(self, first, last, emp_list=None):
        Employee.__init__(self, first, last)
        if emp_list is None:
            self.emp_list = []
        else:
            self.emp_list = emp_list

    @LoggerDecorator
    def add_emp(self, emp):
        for i in emp:
            self.emp_list.append(i)

    def __str__(self):
        msg = super().__str__() + ' number of direct report = {}'.format(len(self.emp_list))
        return msg

    @LoggerDecorator
    def temp(self):
        time.sleep(2)
