# def function1():
#     print("hi hero")

# func2 = function1  # it make copy of function1
# del function1 # it delete function1
# func2()


# return function through a function
# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum

# a = funcret(1)
# print(a)


# we can give function as an argument in a function
# def executer(func):
#     func("this")

# executer(print)


# Decorators -> it is function which takes function as an argument
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

def what_is_your_name():
    print("my name is akash")

name_please = dec1(what_is_your_name)
name_please()
    
        
        