# Map -> it apply a single function on all elements of the list

# numbers = ["8","3","65","33"]

# # for i in range (len(numbers)):
# #     numbers[i] = int(numbers[i])

# numbers = list(map(int, numbers))

# numbers[2] = numbers[2] + 1
# print(numbers[2])

# num = [2,3,4,5,6,7,8,9]
# square = list(map(lambda x: x*x , num))
# print(square)

#############################################################
# filter

# list_1 = [1,4,2,6,8,3,5,9,10]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list(filter(is_greater_5 ,list_1))
# print(gr_than_5)

##############################################################
# Reduce
from functools import reduce
  
list_2 = [3,5,8,12,45]

# num = 0
# for i in list_2:
#     num = num + i

num = reduce(lambda x,y:x+y ,list_2)

print(num)
