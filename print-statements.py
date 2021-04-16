"""
print("my name is khan", end=" ")
print("and i am not a terrorist")
print("my name is khan","and i am not a terrorist")
print("\"my name is khan\"")

# \t = it give a space between words 
# \n = it change line 

## variables 
var1 = "hello world "
var4 = "Akash"
var2 = 4
var3 = 45.6
print(type(var1))
print(type(var2))
print(type(var3))
print(var1 + var4)

var5 = "56"
var6 = "44"
print(var5 + var6)
print(int(var5) + int(var6)) # convert string into int

print(10 * "hello world\n")

# to take input from the user
print("Enter a number")
x = input() # it take input in form of string

print("you entered ",x)
print("you entered ",int(x)+4)
"""

########################################################################
# F-string 
import math

me = "Akash"
a1 = "1army"
# a = f"my irctc account name is {me}{a1}"
a = f"my account name is {me}.{math.cos(65)}"
print(a)
