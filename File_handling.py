# File IO Basics
"""
"r" -> Read Mode (open file for reading) --> default mode
"w" -> Write Mode (Open file for writing)
"x" -> Creates file if not exists
"a" -> Add more content to a file
"t" -> text mode (open file in text mode)
"b" -> binary mode
"+" -> Read and write both
"""

############ read file ##################

# f = open("Akash.txt", "rt")
# content = f.read()
# content = f.read(3)
# print("1",content)
# content = f.read(3)
# print("2",content)

# for line in f:
#     print(line, end="")

# print(f.readline())
# print(f.readline())

# print("2", content)
# print(f.readlines())
# f.close()

############ write file ###############
# f = open("Akash2.txt", "w")
# a = f.write("akash to ekdam heavy driver nikla\n")
# print(a)
# f.close()

########## append mode ################
# f = open("Akash2.txt", "a")
# a = f.write("akash mauj kra dii betey\n")
# print(a)
# f.close()

######### Handle read and write Both ###########
# f = open("Akash2.txt", "r+")
# print(f.read())
# f.write("thank you")
# f.close()

######### more functions on file IO ############
# f = open("Akash.txt")
# print(f.tell()) # it tells where our file pointer is
# print(f.readline())
# print(f.tell())

# f.seek(10)  # it bring file pointer in given position
# print(f.readline())
# f.close()

######## using with block to read/write file ###########
# with open("Akash.txt") as f:
#     a = f.read(4)
#     print(a)
    