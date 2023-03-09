#inhertiance allows us to inherit attribute and methods from the parent classes

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

class Developer(employee): #Developer subclass is inherting attributes of the employee parent class
    raise_amount = 1.10 #the first thing the program checks is the Developer class first 

    def __init__(self, first, last, pay, email, prog_lang):
        super().__init__(first,last,pay,email)
        self.prog_lang = prog_lang

class Manager(employee):
    def __init__(self, first, last, Pay, email, employees = None):
        super().__init__(first, last, Pay, email)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname(), emp.email, emp.pay, emp.prog_lang)


dev_1 = Developer ('Pareekshit', 'pokharel', 50000, 'pareekshit.pokharel@gmail.com', 'Python') 
dev_2 = Developer('Jabeen', 'shrestha', 80000, 'jabeen.shrestha@gmail.com', 'Java') 


manager_1 = Manager('Dinesh', 'Pokharel', 50000, 'dinesh.pokharel@gmail.com',[dev_1])

manager_1.add_emp(dev_2)

manager_1.print_emp()

manager_1.remove_emp(dev_1)

manager_1.print_emp()

