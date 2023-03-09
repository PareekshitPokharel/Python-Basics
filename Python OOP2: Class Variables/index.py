#CLASS VARIABLES ARE THOSE THAT ARE SHARED AMONG ALL THE ISNTANCES OF A CLASS
#WHILE ISNTANCE VARIABLES CAND BE UNIQUE FOR EACH ISNTANCE LIKE OUR EMAIL, NAME AND PAY
#CLASS VARIABLE WILL BE THE SAME AMONG ALL THE ISNTANCES
#NOW THINK WHAT WOULD BE THE COMMON VARIABLE AMONG THE EMPLOYEE CLASS? MAYBE THE ANNUAL RAISE???
#HENCE WE CAN KEEP THE ANNUAL RAISE AS THE CLASS VARIABLE SO THEY CAN BE ACCESSED BY ALL THE DATA
class employee:

    raise_amount = 1.04 #This is called the class variable accessible by each instances
    num_of_emps = 0

    def __init__(self, first, last, Pay, email): #This is called instances
        self.first = first #These are instance variables
        self.last = last
        self.pay = Pay
        self.email = email

        employee.num_of_emps += 1 #this code is written here because init runs everytime we add a new employee
    
    def fullname(self): 
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #the class variable can be accessible only by class method or self method employee.raise_amount or self.raise_amount

emp_1 = employee ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com') #These are our isntances
emp_2 = employee('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com') #These are our instances