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



akash_bharadwaj = Employee("akash","bharadwaj")
rishi_bharti = Employee("rishi","bharti")

print(akash_bharadwaj.email)

# by using property function
akash_bharadwaj.fname = "prakash"
print(akash_bharadwaj.email)

# by using setter
akash_bharadwaj.email = "abra.ka@dabra.com"
print(akash_bharadwaj.fname)

# by using deleter
del akash_bharadwaj.email
print(akash_bharadwaj.email)