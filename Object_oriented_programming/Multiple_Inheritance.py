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

class Player:
    game = "volleyball"

    def print_sports_details(self): 
        return f"the name is {self.name} and game is {self.game}"
    

class Coolprogrammer(Employee , Player): # here order is very important
    language = "c++"

    def print_language(self):
        print(self.language)
    
        

harry = Employee("Harry", 255 ,"Instructor")
akash = Coolprogrammer("Akash", 500 ,"coder")

akash.print_language()
print(akash.print_sports_details())

