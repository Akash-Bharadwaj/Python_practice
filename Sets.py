# Set can be easily made by using list

s = set() #empty set
# print(type(s))

# s_from_list = set([1,2,3,4,5])
# l = [1,2,3,4,5]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))

# Add elements in empty set
s.add(1)
s.add(1)
s.add(2)
# print(s)
print(min(s))
s1 = s.union({1,2,4,5})
s2 = s.intersection({1,2,4,5})
print(s,s1,s2)
print(s.isdisjoint(s1))