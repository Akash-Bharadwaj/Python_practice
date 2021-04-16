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

    # class-method -> it act as a decorator which take class as an argument
    @classmethod
    def change_leaves(cls, newleaves): # here cls is 'class Employee'
        cls.no_of_leaves = newleaves

    # class-methods as a constructor
    @classmethod
    def str(cls, string):
        # value = string.split("-")
        # return cls(value[0],value[1],value[2])
        return cls(*string.split("-"))  # one liner code by args

    @staticmethod
    def printgood(string):
        print("this is good "+ string)
        
    

ravan = Employee("ravan" , 50000 , "Boss")
ravan.change_leaves(56)  
print(ravan.no_of_leaves)
print(Employee.no_of_leaves) # here attributes of class is also get changes

# after using class-methods as constructer
rohan = Employee.str("rohan-60000-scientist")
print(rohan.role)

# for staticmethod
Employee.printgood("Akash")


# abstraction -> kaam ko tukre may baant ker kerna 
# Encapsulation -> sirf product ko use kerna , uska pura information hide kerna 