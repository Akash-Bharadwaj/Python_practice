# l = 10 # Global (cant be changed in local scope)
# def function1(n):
#     # l = 5   # local (can be change)
#     m = 8
#     l = l + 45
#     print(l,m)
#     print(n,"I have printed")
    
# function1("this is me,")
# print(l)

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 98
    # print("before calling rohan()", x)
    rohan()
    print("After calling rohan()", x)
    
harry()   
print(x)
