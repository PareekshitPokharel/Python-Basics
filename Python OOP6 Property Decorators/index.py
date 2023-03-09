class employee:

    def __init__(self, first, last, email): 
        self.first = first 
        self.last = last
        self.email = email

    @property #can be used function like a method and not like a function 
    def fullname(self): 
        return f'{self.first} {self.last}'



emp_1 = employee ('Pareekshit', 'pokharel', "pareekshit.pokharel@gmail.com") 
emp_2 = employee('Jabeen', 'shrestha', 'jabeen.shrestha@gmail.com') 

 
print(emp_1.fullname) #for example here without the parentheses