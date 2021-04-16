# classes -> Template
# object -> item created based on that particular Template
#             or  (Instance of the classes)

# OOPS works on a concept of "DRY"(Don't Repeat Yourself)

###########################################################################

class Student:
    pass

harry = Student() # instance variables
akash = Student()

harry.name = "Harish"
harry.std = 12
harry.sed = 1
akash.name = "Bambam"
akash.std = 12
akash.sed = 2

print(harry.name, akash.name)
