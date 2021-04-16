a = 34
b = 54
# c = sum((a , b))  # built-in function

def func1(a,b):
    print("hello you are in function1", a+b)

def func2(a,b):
    """This is a function which print average of two numbers"""   # this is a docString
    avg = (a+b)/2
    return avg

func1(5,7)

print(func2.__doc__)
v = func2(5,7)
print(v)


##########################################################################
# lambda function -> it is a one line function

# def add(a,b):
#     return a+b

# add1 = lambda x,y : x+y
# print(add1(5,6))

# a = [[1,14],[5,6],[8,23]]
# a.sort(key=lambda x:x[0]) # it take a function as input which return 1st elenment of list
# print(a)

###########################################################################
# args-&-kwargs

# def function_print_names(a,b,c,d):
#     print(a,b,c,d)

# function_print_names("aki","aku","prakash","akash","bakwash") 
       # it gives error as there is only 4 arguments in this function

# To solve this issue

def funargs(normal , *args , **kwargs):  # normal argument always comes first than args and than kwargs
    # print(args[0])
    for item in args:
        print(f"{normal} {item}")

    print("now i would like to introduce some of our heroes")

    for key ,value in kwargs.items():
        print(f"{key} is a {value}")
        

har = ["harry","rohan","skillf","akash","prakash","shivam"]
army = "band of brothers"
kw = {"Rohan":"Monitor", "harry":"commander", "Akash":"major"}
funargs(army,*har,**kw)