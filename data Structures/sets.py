'''
set:
how to create set:
using  {}
using set()

properties:
1. uordered
2. must be unique
3. can not store duplicate
4. mutable: can not change the items, but structure can be




# x={1,2,3,4,5,9,7}
x=set((1,2,3,4,5,9,7))
print(x)
print(type(x))

# unique
x={1,2,3,4,5,9,7,7}
print(x)

# heterogeneous
x={1,2,"abc",9,7,7}
print(x)


# immutable
x={1,2,3,4,5,9,7,7}
x[2]=5
'''
# x={1,2,3,4,5,9,7,7}
# x[2]=5
# remove(): if that item is not present it will throw an error


""" 
# how to itterate a set
x={1,2,3,4,5,6,7,8,9}
for i in x:
    print(i)
print(x)

# to check item is present or not
if 6 in x:
    print("item found")
else:
    print("item not found")

# remove(): it remove the items from list andif that item is not present it will throw an error
x.remove(2)
# x.remove(22)

print(x)
# discard(): it is similiar to remove(), but it will throw error if item is not present
x.discard(22)
print(x)

# pop():It will remove item randomly
x.pop()
print(x)

# clear(): It will remove all items from set
x.clear()
print(x)

# add(): add single element in set
x.add(5)
x.add(15)
print(x)
#  update(): add multiple items in set

x.update([1,2,3,9,10])
print(x) """

# set operation
""" # union(): it will return the union of two sets except duplicate values
x={1,2,3,4,5}
y={3,4,5,6,7}

# print(x.union(y))
p=x | y #using symbol of union 
print(p)
# intersection(): it will return the intersection of two sets
x={1,2,3,4,5}
y={3,4,5,6,7}

# print(x.intersection(y))
p=x & y #using symbol
print(p)


# intersection update(): it wil update existing set
x={1,2,3,4,5}
y={3,4,5,6,7}
x.intersection_update(y)
print(x) 


# difference and differene update
# difference: it will return difference element only from first
x={1,2,3,4,5}
y={3,4,5,6,7}

# p=x.difference(y)
# print(p)
x.difference_update(y)
print(x)



# symmetric difference and symmetric differene update
x={1,2,3,4,5}
y={3,4,5,6,7}
# p=x.symmetric_difference(y)
# print(p)
x.difference_update(y)
print(x)
# superset
# subset
x={1,2,3,4,5}
y={11,22,33}
print(x.issubset(y))
print(y.issubset(x))

print(x.issuperset(y))
print(y.issuperset(x))

# disjoint:If comman element in both set return false otherwise return true
print(x.isdisjoint(y))

# sorted
x={11,67,3,5,7,35}
print(x)
y=sorted(x)
print(y)

# if we want create something new from existing set/list, then we will prefer comprehension

"""

# frozenset(): It is completely immutable set
x=frozenset({1,2,3,4,5})
# x.add(77) #it will throw error 

# merge frozenset
y=frozenset({10,11,12})
p=(frozenset(x) ,frozenset(y))
print(p)

for i in p:
    print(i)

print(x)
# set comprehension
even={i*i for i in x if i%2==0}
print(even)