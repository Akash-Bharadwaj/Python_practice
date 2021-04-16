class Employee:

    # Constructor
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

    @classmethod
    def str(cls, string):
        return cls(*string.split("-")) 

    @staticmethod
    def printgood(string):
        print("this is good "+ string)



# Inheritance -> it means passing all features of one class to another 
class Programmer(Employee):
    def printprog(self):
        return f"programmer's name is {self.name}, Salary is {self.salary} and role is {self.role} and he knows {self.languages}"

    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages


harry = Employee("Harry", 255 ,"Instructor")
akash = Programmer("Akash", 500 ,"coder","Cpp")

# print(akash.print_details())
print(akash.printprog())
