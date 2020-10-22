#!/usr/bin/env python3

class Employee: # class is blueprint for creating instances
    #pass # only if you have an empty class so it won't cause an error
#2 - __init__ method (initialize/constructor)- automatic
    def __init__(self, first, last, pay): #receives 1st instance (self) automatically
        self.first= first
        self.last= last
        self.pay= pay
        self.email = first + '.' + last + '@company.com'

#4 - note: each method in a class each takes the instance as the first argument, and you're always going to call that self - put it in the parantheses
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


#2 continued
emp_1= Employee('Corey', 'Schafer', 50000) #args must be passed in order
emp_2= Employee('Test', 'User', 60000)

#print(emp_1.email)
#print(emp_2.email) #achieves the same effect as step 1 without so much code

#4 calling on the method to create full name
print(emp_1.fullname()) #<-----need () after fullname bc its a method

#5 you can also run these methods using the class name although it'll be more obvious of what's running in the background
#need to pass the instance as the argument
print(Employee.fullname(emp_1))

#3 - to print emp1's full name using class - but that's a lot of code -> create using a method (#4)
#print('{} {}'.format(emp_1.first, emp_1.last))

#1 - creating employees and specific attributes for each, manually  - prone to mistakes and a lot of code
#emp_1 = Employee()
#emp_2 = Employee() #each emp is unique instance of Employee class

# print(emp_1)
# print(emp_2) #both are Employee objects but each are unique bc they have different instances in memory i.e. 0x7f8f28b00910 vs. 0x7f8f28b00960

# emp_1.first='Corey'
# emp_1.last='Schafer'
# emp_1.email='Corey.Schafer@company.com'
# emp_1.pay=50000

# emp_2.first='Test'
# emp_2.last='User'
# emp_2.email='Test.User@company.com'
# emp_2.pay=60000

