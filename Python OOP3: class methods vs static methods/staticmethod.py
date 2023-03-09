class employee:

    raise_amount = 1.04 
    num_of_emps = 0

    def __init__(self, first, last, Pay, email): 
        self.first = first 
        self.last = last
        self.pay = Pay
        self.email = email

        employee.num_of_emps += 1 
    
    def fullname(self): 
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    #Class variables can be used to directly access the class

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay, email = emp_str.split('-')
        return cls(first, last, pay, email)

    @staticmethod
    def is_workday(day): #Note static method don't take instances like self nor class like cls so we passed in the variable day
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = employee ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com') 
emp_2 = employee('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com') 


import datetime

my_date = datetime.date(2016,7,10)
print(employee.is_workday(my_date))


#NOTE:
#   REGULAR METHOD AUTOMATICALLY PASS INSTANCE AS THE FIRST ARGUMENT CALLED AS SELF
#   CLASS METHOD AUTOMATICALLY PASS INSTANCE AS THE FIRST ARGUMENT CALLED AS CLS  
#   STATIC METHOD DO NOT PASS ANYTHING AUTOMATICALLY AND BEHAVE LIKE REGULAR FUNCTION
#   BUT WE INCLUDE THEM IN OUR CLASSES BECAUSE THEY HAVE SOME LOGICAL CONNECTION WITH THE CLASS



 