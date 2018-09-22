import class_def as defs
import random
import time
import mem_profile
import sys

firstname = ['Hirad', 'Bahar', 'Nooshin', 'Ali', 'Farhang']
lastname = ['Karimi', 'Amiri', 'Doe', 'Clay', 'Jalilian']


def people_list (num):

    temp = []
    for i in range(num):
        temp.append(defs.Employee(random.choice(firstname), random.choice(lastname)))
    return temp


def people_generator(num):

    for i in range(num):
        yield defs.Employee(random.choice(firstname), random.choice(lastname))

# emp1 = defs.Employee.from_string('hirad karimi')
# emp2 = defs.Developer.from_string('Bahar Amiri,5000')
# mng1 = defs.Manager.from_string('Nooshin Karimi')
# mng1.add_emp([emp1])


t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory : {}Mb'.format(sys.getsizeof(people)))
print('Took {} Seconds'.format(t2-t1))