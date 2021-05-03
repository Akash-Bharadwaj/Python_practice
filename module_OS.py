import os
# print(dir(os)) 

print(os.getcwd())

# # to change our working directiory
# os.chdir("D://")
# print(os.getcwd())

# to check the files on current directiory
# print(os.listdir())
# print(os.listdir("D://"))

# # To create a new folder in working Directiory
# os.mkdir("This") # it make only one folder
# os.makedirs("This/That") # it make folder inside a folder

# to rename a file
# os.rename("Akash.txt" , "akash.txt")

print(os.path.join("D://","Akash"))


# to check wether the path is correct or not
# print(os.path.exists("D://"))

# to check wether the file is exist or not
print(os.path.isdir("D://Akash"))


