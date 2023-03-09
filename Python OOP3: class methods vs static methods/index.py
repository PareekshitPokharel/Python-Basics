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

emp_1 = employee ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com') 
emp_2 = employee('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com') 

emp_str_1 = 'John-Doe-7000-john.doe@gmail.com'
emp_str_2 = 'Steve-Smith-3000-steve-smith@gmail.com' 

new_emp = employee.from_string(emp_str_1)
print(new_emp)
