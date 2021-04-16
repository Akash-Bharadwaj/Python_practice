d1 = {}
print(type(d1))

d2 = {"india":"Rafale", "pakistan":"f16", "USA":"f22", "russia":{"fighter":"su35", "bomber":"su33"}}
d2["china"] = "j10"
d2["england"] = "Eurofighter typhoon"
print(d2)
# print(d2["USA"])
# print(d2["russia"]["bomber"])

# del d2["pakistan"]
# print(d2)

# d3 = d2.copy()
# del d3["china"]
# print(d3)

d2.update({"france":"rafale"})
print(d2)

print(d2.keys())

print(d2.items())

# Making dictionary from list
list1 = [ ["Harry",1] ,["larry",4],["Carry",7] ,["Marie",3] ]

dict1 = dict(list1)
print(dict1)