class Employee:
    def __init__(self ,fname , lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self ,string):
        names = string.split("@") [0]
        self.fname = names.split(".") [0]
        self.lname = names.split(".") [1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


# object_Introspection -> collecting full information about object

rishi_bharti = Employee("rishi","bharti")
print(rishi_bharti.email)

print(type(rishi_bharti))
print(dir(rishi_bharti))

import inspect
print(inspect.getmembers(rishi_bharti))
