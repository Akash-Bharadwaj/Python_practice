# Super() -> it is used to call the constructer of main class

class A:
    classvar1 = "I am a class variable of class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructer"
        self.classvar1 = "Instance variable in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):         # here this __init__ override the __init__ constructor of class-A , 
        super().__init__()                  # hence to call class-A's constructor , we use super function

        self.var1 = "I am inside class B's constructer"
        self.classvar1 = "Instance variable in class B"
        

a = A()
b = B()

print(b.special, b.var1, b.classvar1)
