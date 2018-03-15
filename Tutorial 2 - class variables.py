# T2 - CLASS VARIABLES
# instance var = unique for each instance, eg. names, pays and mails
# class var = shared among all instances in a class
class Employee2_1:
    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.mail = str(firstname + '.' + lastname + '@company.com')

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    # create a method called apply_raise
    def apply_raise(self):
        self.pay = int(self.pay * (1 + 0.04))
        return self.pay

emp_21 = Employee2_1('Mandie','He',66666666)
emp_22 = Employee2_1('John','Doe',111111)

print(emp_21.pay)
print(emp_21.apply_raise())

# what if i want to easily update the raise amount?
# using class var could avoid u from updating by changing multiple places
# to set up/ define a class variable
# use a declaration statement after defining class

class Employee2_2:
    # defining a class variable
    raise_amount = 0.04

    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.mail = str(firstname + '.' + lastname + '@company.com')

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * (self.raise_amount + 1))

emp_23 = Employee2_2('Mandie','He',66666666)
emp_24 = Employee2_2('John','Doe',111111)

print(Employee2_2.raise_amount) # 0.04
print(emp_23.raise_amount) # 0.04
print(emp_24.raise_amount) # 0.04, the same results would indicate that we can access the class var from both class itself and the instances
# the instances 'emp_23' and 'emp_24' don't contain the attribute 'raise_amount' themselves
# the attribute 'raise_amount' is heritaged from the class 'Employee2_2'

print(emp_24.pay) # 111111
emp_24.apply_raise() # raising the payment for emp_24 for 111111*0.04 = 4444.44
print(emp_24.pay)

# to print the namespace of emp_23
print(emp_23.__dict__) # {'first': 'Mandie', 'last': 'He', 'pay': 66666666, 'mail': 'Mandie.He@company.com'}
print(Employee2_2.__dict__)
"""{'__module__': '__main__', 
'raise_amount': 0.04, '__init__': <function Employee2_2.__init__ at 0x03720198>,
'fullname': <function Employee2_2.fullname at 0x03720150>, 
'apply_raise': <function Employee2_2.apply_raise at 0x03720108>, 
'__dict__': <attribute '__dict__' of 'Employee2_2' objects>, 
'__weakref__': <attribute '__weakref__' of 'Employee2_2' objects>, 
'__doc__': None}
"""
# the printed strings above also shows that attribute 'raise_amount' is only contained in the class rather than being contained in the instance

# now we update the raise amount and re-run the payment computation code
Employee2_2.raise_amount = 0.05
print(emp_23.pay) # 66666666
emp_23.apply_raise() # raising the payment for emp_24 for 66666666*0.05 = 3333333
print(emp_23.pay) # 69999999

# and you can see the update modified  the raise amount for both class and instances
print(Employee2_2.raise_amount) # 0.05
print(emp_23.raise_amount) # 0.05
print(emp_24.raise_amount) # 0.05

# if only attribute 'raise amount' for specific stances is considered to be changed
# just update the value of attribute for that SPECIFIC STANCES using an assignment
emp_23.raise_amount = 0.06
print(Employee2_2.raise_amount) # 0.05
print(emp_23.raise_amount) # 0.06, which is the only that has been modified
print(emp_24.raise_amount) # 0.05

# currently, emp_23 contains the attribute of 'raise_amount' as shown in the following printed-out
print(emp_23.__dict__) # {'first': 'Mandie', 'last': 'He', 'pay': 69999999, 'mail': 'Mandie.He@company.com', 'raise_amount': 0.06}


# another example would be a counter, counting how many emps are contained in the class
# we still firstly create a class
class Employee2_3:

    num_of_emps = 0 # now we add a counter as a class variable, starting from 0, and increment by one as we create an emp as an instance
    raise_amount = 0.04

    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.mail = str(firstname + '.' + lastname + '@company.com')
        # now adding the looping equation in the defining statement of __init__ method
        Employee2_3.num_of_emps += 1 # we do not use 'self.num_of_emps' because, the no. of emps would be the same for each instance
print(Employee2_3.num_of_emps) # 0
emp_25 = Employee2_3('Mandie','He',66666666)
emp_26 = Employee2_3('John','Doe',111111)
# but after adding emps
print(Employee2_3.num_of_emps) # 2
