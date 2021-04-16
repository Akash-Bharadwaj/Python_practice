class Employee:
    no_of_leaves = 8  
    
    # Constructor
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # Methods
    def print_details(self): # here "self" means that object which use this function
        return f"Name is {self.name}, Salary is {self.salary} and role is {self.role}"


ravan = Employee("ravan" , 50000 , "Boss")
print(ravan.print_details())
print(ravan.role)