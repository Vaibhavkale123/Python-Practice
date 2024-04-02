
# tuples python.txt

# 1. Write a Python program to create a tuple. 
x=(1,2,3,4,5)#create using'()'
y=tuple((6,7,8,9))#created using tuple()
print(x)
print(y)




# 2. Write a Python program to create a tuple with different data types. 
x=(1,2,'Hello',3.0)     
print(x)

# 3. Write a Python program to create a tuple of numbers and print one item. 
x=(1,2,3,4)
print(x[2])
print(x[1])



# 4. Write a Python program to unpack a tuple into several variables. 
x=1,2,3,4,5
a,b,c,d,e=x
print(a)
print(b)
print(c)



# 5. Write a Python program to add an item to a tuple. 
x=(1,2,3,4,5)
x=list(x)
x.append(9)
x=tuple(x)
print(x)

# 6. Write a Python program to convert a tuple to a string. 



# 7. Write a Python program to get the 4th element from the last element of a tuple. 
x=1,2,3,4,5

print(x[3])

# 8. Write a Python program to create the colon of a tuple. 
# Create a tuple using the colon operator


# 9. Write a Python program to find repeated items in a tuple. 
x = (1,2,3,5,2,5,3)
r=set()
for i in x:
    if x.count(i)>1:
        r.add(i)
print("repeated items",len(r))


# 10. Write a Python program to check whether an element exists within a tuple. 

x = (1,2,3,5,2,5,3)
if 2 in x:
    print("5 is exist in tuple")
else:
    print("5 is not exist in tuple")
    


# 11. Write a Python program to convert a list to a tuple. 
x=[1,2,3,4,5]
x=tuple(x)
print(type(x))
print(x)



# 12. Write a Python program to remove an item from a tuple. 

x = (1,2,3,5,2,5,3)
print("before removing from tuple: ",x)
x=list(x)
x.remove(2)
x=tuple(x)
print("after removing from tuple: ",x)


# 13. Write a Python program to slice a tuple. 
x = (1,2,3,5,2,5,3)
print(x[1:5:2])


# 14. Write a Python program to find the index of an item in a tuple. 
x = (1,2,3,5,2,5,3)
print(x.index(2))


# 15. Write a Python program to find the length of a tuple. 
x = (1,2,3,5,2,5,3)
print(len(x))



# 16. Write a Python program to convert a tuple to a dictionary. 



# 17. Write a Python program to unzip a list of tuples into individual lists. 



# 18. Write a Python program to reverse a tuple. 
x = (1,2,3,5,2,5,3)
x=list(x)
x.reverse()
x=tuple(x)
print(x)



# 19. Write a Python program to convert a list of tuples into a dictionary. 



# 20. Write a Python program to print a tuple with string formatting. 
