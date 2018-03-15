# T1 - CLASSES AND INSTANCE VARIABLES

# to create an empty class
class Employee1_1:
    pass    # leaving the class empty

emp_11 = Employee1_1()
emp_12 = Employee1_1()
print(emp_11)  #<__main__.Employee object at 0x02D8FAF0>
print(emp_12)  #<__main__.Employee object at 0x02D8FBD0>

# to create an instance variable, which contains unique data for each instance
emp_11.firstname = "Mandie"
emp_11.lastname = "He"
emp_11.mail = "MandieHe@company.com"
emp_11.pay = 66666666

emp_12.firstname = "Johnney"
emp_12.lastname = "Whooston"
emp_12.mail = "Johnney@company.com"
emp_12.pay = 1111111

# to print out instance variables
print(emp_11.mail)  #amahe@company.com
print(emp_12.mail)  #jwh@company.com

# but input the info relatively for each would be inconv
# so we create a __init__ method to avoid that
class Employee1_2:
    def __init__(self, firstname, lastname, pay): # you can add args
        # the instance 'self' would be auto'ly added
        self.first = firstname # format is """self.var_name = arg_name"""
        self.last = lastname
        self.pay = pay
        self.mail = str(firstname + '.' + lastname + '@company.com')
        self.email = self.first + '.' + self.last + '@company.com'

emp_13 = Employee1_2('Mandie','He',66666666)
emp_14 = Employee1_2('John','Doe',111111)

# to print out the instance variables
print(emp_13.mail)
print(emp_14.email) # pay attention to the expression of 'self.mail' & 'self.email'

# to add attributes outside the class
print('{} {}'.format(emp_13.first,emp_13.last))

# to add methods other than __init__
class Employee1_3:
    def __init__(self, firstname, lastname, pay):
        self.first = firstname
        self.last = lastname
        self.pay = pay
        self.mail = str(firstname + '.' + lastname + '@company.com')

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp_15 = Employee1_3('Mandie','He',66666666)
emp_16 = Employee1_3('John','Doe',111111)

print(emp_15.fullname()) # Mandie He
print(emp_16.fullname()) # John Doe
print(Employee1_3.fullname(emp_16)) # John Doe
