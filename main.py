import class_def as defs
import random
import time
import sys
import logging

firstname = ['Hirad', 'Bahar', 'Nooshin', 'Ali', 'Farhang']
lastname = ['Karimi', 'Amiri', 'Doe', 'Clay', 'Jalilian']

logger = logging.getLogger('Main')
formatter = logging.Formatter('%(name)s: Line %(lineno)s: %(filename)s: %(message)s')
f_handler = logging.FileHandler(filename='sample.log')
logger.setLevel(logging.DEBUG)
f_handler.setFormatter(formatter)
logger.addHandler(f_handler)

logger.info('here in the main.py')

def people_list (num):

    temp = []
    for i in range(num):
        temp.append(defs.Employee(random.choice(firstname), random.choice(lastname)))
    return temp


def people_generator(num):

    for i in range(num):
        yield defs.Employee(random.choice(firstname), random.choice(lastname))

emp1 = defs.Employee.from_string('hirad karimi')
emp2 = defs.Developer.from_string('Bahar Amiri,5000')
mng1 = defs.Manager.from_string('Nooshin Karimi')
mng1.add_emp([emp1])
mng1.temp()


t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory : {}Mb'.format(sys.getsizeof(people)))
print('Took {} Seconds'.format(t2-t1))