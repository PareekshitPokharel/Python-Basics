class employee:
    def __init__(self, first, last, Pay, email): #the emp1 and emp2 of the taditional approach has been replaced by self method
        self.first = first #self is the isntance here 
        self.last = last
        self.pay = Pay
        self.email = email
    
    def fullname(self): #each method within the class automatically takes instances as the first argument so init will be printed first
        return f'{self.first} {self.last}'

emp_1 = employee ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com') #HERE THE EMP_1 WILL BE PASSED AUTOMATICALLY AS THE SELF
emp_2 = employee('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com')

print(emp_1.fullname()) #while using the method without the class we should not pass anything in the parameter because the self will pass by itself
print(employee.fullname(emp_1)) #while using the class we should pass the instances as well 


        
