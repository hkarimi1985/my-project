import class_def as defs
import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG, format='%(asctime)s: %(filename)s: %(message)s')

emp1 = defs.Employee.from_string('hirad karimi')
emp2 = defs.Developer.from_string('Bahar Amiri,5000')
mng1 = defs.Manager.from_string('Nooshin Karimi')
mng1.add_emp([emp1,emp2])

defs.Employee.get_num_of_employee()