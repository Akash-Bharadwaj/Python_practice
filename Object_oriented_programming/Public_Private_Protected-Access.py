# Public variables -> used within any class
# Protected variables -> used within main class and the class inheritate with main class
# Private variables -> used within main class only

class Employee:
    var = 8
    _protect = 9
    __private = 98

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


harry = Employee("Harry", 255 ,"Instructor")
# print(harry.var)
# print(harry._protect)
# print(harry.__private) # it gives error
print(harry._Employee__private)
