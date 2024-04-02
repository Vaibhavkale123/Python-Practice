""" '''
tupels:
how to create a tuple?
1. using ()
2. using tuple()

characteres:
1. Immualbe 
2. ordered
3. Index based
4. heterogenous data types
5. allow duplicate values
'''
x = 1, 2, 3

#find the element with index:
print(x[1])

# packing and unpacking tuples:
x = 1, 2, 3



a, b, c = x
print(x)
print(type(x))
print(a,b,c)

# iterating over a tuple:
for i in x:
    print(i)

#you can only  remove elements from a tuple by converting into list:
#  find occurances of an element in a tuple:
x=1,2,2,9,3,2,8,4
print(x.count(2))

# concation of tuple
x = (1,2)
y=(3,4)
p= x+y
print(p)
# using sum()
q=sum((x,y),())
print(q)


# nested tuples:
x=((1,2),(2,3),(3,4))
for i in x:
    print("tuple ",i," elements")
    for j in i:
        print(j,end=" ")
    print()
 """
# 1. Write a Python program to find repeated items in a tuple.

x = (1,2,3,5,2,5,3)
r=set()
for i in x:
    if x.count(i)>1:
        r.add(i)
print("repeated items",len(r))


# 2. Write a Python program to check whether an element exists within a tuple. 

x = (1,2,3,5,2,5,3)
if 2 in x:
    print("2 is exist in tuple")
else:
    print("2 is not exist in tuple")
    

# 3. Write a Python program to convert a list to a tuple.
x = [1,2,3,5,2,5,3]
x=tuple(x)
print("type of x: ",type(x),)


# 4. Write a Python program to remove an item from a tuple.
x = (1,2,3,5,2,5,3)
print("before removing from tuple: ",x)
x=list(x)
x.remove(2)
x=tuple(x)
print("after removing from tuple: ",x)
