# Pickle module is used to preserve an object(list , dictionary , variable etc) in a binary 
# formated file which we can use later using pickle module again


import pickle

# Pickling a python object

# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

# extracting our object from pickle file

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))