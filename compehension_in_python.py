# list comprehensions 

# ls = []
# for i in range(100):
#     if i%3 == 0:
#         ls.append(i)

# we can do this in one line of code 

ls = [i for i in range(100) if i%3==0]
print(ls)

# Dictionary comprehensions

dict1 = {i:f"item{i}" for i in range(1 , 100) if i%10 == 0}
print(dict1)
# to reverse a dictionary 
dict2 = {value:key for key,value in dict1.items()}
print(dict1 , "\n" , dict2)

# generators comprehension

evens = (i for i in range(100) if i%2 == 0)
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

for items in evens:
    print(items)
    
