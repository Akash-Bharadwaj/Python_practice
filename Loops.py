# for_loop in python

list1 = [ ["Harry",1] ,["larry",4],["Carry",7] ,["Marie",3] ]

# for item , lollypop in list1:
#     print(item, "and he eats" ,lollypop , "lollypop")

dict1 = dict(list1)
# print(dict1)

# for item , lollypop in dict1.items():
#     print(item, "and he eats" ,lollypop , "lollypop")

# for item , lollypop in dict1.items():
#     print(lollypop)

# using Else with for loop
khana = ["roti","sabzi" , "chawal"]

for item in khana:
    if item == "roti":
        print(f"chotu wo 4 no. tabel per {item} laga")
        break

else:
    print("bhaiya avi bna nehi hay ")
    
        

# Quiz
items = ["ak47" , "ak103" ,"ak203" ,5,7,2,9,12,23,65,78,32,12,73]

for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)

#######################################################################
# while_loop in python

i = 0

# while(i<20):
#     print(i)
#     i = i+1

# while(True):
#     if i+1 < 5:
#         i += 1
#         continue
#     print(i+1, end=" ")
#     if(i == 44):
#         break   #stop the loop
#     i = i+1

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have enter a number greater than 100")
        break
    else:
        print("try again")
        continue