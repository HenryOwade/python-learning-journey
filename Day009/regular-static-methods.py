# Regular methods and static methods

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "first" + "." + "last" + "@company.com"

        Employee.num_of_emps += 1
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    print(num_of_emps)
    
emp_1 = Employee("Henry", "Owade", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.pay)

Employee.raise_amount = 1.05
emp_1.pay = int(emp_1.pay * emp_1.raise_amount)


emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(Employee.num_of_emps)


