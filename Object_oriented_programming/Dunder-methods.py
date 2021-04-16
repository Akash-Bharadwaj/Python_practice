class Employee:

    # Constructor -> it is also a dunder method
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # Methods
    def print_details(self): 
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves

    # Dunder-Methods  -> by using this we do object overloading
    def __add__(self ,others):
        return self.salary + others.salary

    def __repr__(self):
        return f"Employee('{self.name}' , {self.salary} , '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"

emp1 = Employee("Akash" , 345 , "coder")
emp2 = Employee("perkash" , 300 , "programmer")
# print(emp1 + emp2)
print(emp1) # it print str over repr 

    