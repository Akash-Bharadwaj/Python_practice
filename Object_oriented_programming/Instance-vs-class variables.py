class Employee:
    no_of_leaves = 8  # class variables , equal for all objects of that class
    pass

harry = Employee() # instance variables
akash = Employee()

harry.name = "Harish"
harry.salary = 40000
harry.role = "instructor"

akash.name = "Bambam"
akash.salary = 30000
akash.role = "Student"

print(Employee.no_of_leaves)
print(harry.no_of_leaves)

harry.no_of_leaves = 12  # it does not change class variables, it create new instance variable 
print(harry.__dict__)       
print(harry.no_of_leaves)
print(Employee.no_of_leaves)

Employee.no_of_leaves = 14
print(Employee.no_of_leaves)
print(akash.no_of_leaves)
