#special methods in python are surrounded by doubel udnerscore __
#these double udnerscore are also known as dunder



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

    def __repr__(self): #unambigious representation of the object used for debugging and logging
        return "employee('{}' , '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self): #Readable representation of the object and meant to be used for displaying the object to end-user
        return "{} {}".format(self.first, self.fullname)

    def __add__(self, other): #simply adds to number using this method
        return self.pay + other.pay

    def __len__(self): #counts the value of a string using this method
        return len(self.fullname())    


emp_1 = employee ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com') 
emp_2 = employee('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com') 



print(emp_1.__len__())

# print(emp_1.__repr__())
# print(emp_2.__str__())