# we canot store large data in ram 
# so we use generators to which puts all these data in standby and generate it whenever we need it.

def gen(n):
    for i in range(n):
        yield i

g = gen(35353462345)
print(g)

# iterators method

h = "harry"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())

