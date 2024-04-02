""" 

Set_Assignments.txt
"""

# 1. Write a Python program to create a set.
x={1,2,3}
y=set((5,7,8))# using set()
print(x)
print(y)

# 2. Write a Python program to iterate over sets.
x={1,2,3}

for i in x:
    print(i)

# 3. Write a Python program to add member(s) to a set.
x={1,2,3}
y=int(input("enter item to add in set: "))
x.add(y)
print(x)


# 4. Write a Python program to remove item(s) from a given set.
x={1,2,3}
x.remove(2)
print(x)

# 5. Write a Python program to remove an item from a set if it is present in the set.
x={4,1,2,3}
print(x)

if 4 in x:
    x.remove(4)
print(x)

# 6. Write a Python program to create an intersection of sets.
x={4,1,2,3,5}
y={3,2,5,8,9}
print(x & y)


# 7. Write a Python program to create a union of sets.
x={4,1,2,3,5}
y={3,2,5,8,9}
print(x | y)

# 8. Write a Python program to create set difference.
x={4,1,2,3,5}
y={3,2,5,8,9}
print(x.difference(y) )
print(y.difference(x) )

# 9. Write a Python program to create a symmetric difference.
x={4,1,2,3,5}
y={3,2,5,8,9}
print(y.symmetric_difference(x) )


# 10. Write a Python program to check if a set is a subset of another set.
x={4,1,2,3,5,8,9}
y={3,2,5}
print(x.issubset(y))
print(y.issubset(x))


# 11. Write a Python program to create a shallow copy of sets.
# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact
# copy of the values in the original object.
x={4,1,2,3,5,8,9}
y=x.copy()
y.add(10)
print(y)
print(x)


# 12. Write a Python program to remove all elements from a given set.
x={4,1,2,3,5,8,9}
x.clear()
print(x)


# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.
x= frozenset([12,15])
print(x)

# 14. Write a Python program to find the maximum and minimum values in a set.
x={4,1,2,3,5,8,9}
max=max(x)
print(max)
min=min(x)
print(min)

# 15. Write a Python program to find the length of a set.
x={4,1,2,3,5,8,9}
print(len(x))

# 16. Write a Python program to check if a given value is present in a set or not.
x={4,1,2,3,5,8,9}
n=2
if n in x:
    print("value is present in set")
else:
    print("value is not present in set")


# 17. Write a Python program to check if two given sets have no elements in common.
x={4,1,2,3,5,8,9}
y={11,25,18,1,2}


# 18. Write a Python program to check if a given set is a superset of itself and a superset of
# another given set.
x={4,1,2,3,5,8,9}
y={3,2,5}
print(x.issuperset(x))
print(x.issuperset(y))


# 19. Write a Python program to find elements in a given set that are not in another set.
x={4,1,2,3,5}
y={3,2,5}
print(x.difference(y))

# 20. Write a Python program to remove the intersection of a second set with a first set.
x={4,1,2,3,5}
y={3,2,5}
p=x.intersection(y)
for i in p:
    x.remove(i)
print(x)

# 21. Write a Python program to find all the unique words and count the frequency of occurrence
# from a given list of strings. Use Python set data type.

# 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a
# given value.

# 23. Write a Python program to find the longest common prefix of all strings. Use the Python set.

# 24. Write a Python program to find the two numbers whose product is maximum among all the
# pairs in a given list of numbers. Use the Python set.

# 25. Given two sets of numbers, write a Python program to find the missing numbers in the
# second set as compared to the first and vice versa. Use the Python set.
x={4,1,2,3,5}
y={3,2,5}
print(x)
print(y)
print("number missing in 2nd set compared to first set",x.difference(y))
print("number missing in 1st set compared to second set",y.difference(x))

# 26. Write a Python program to find all the anagrams and group them together from a given list of
# strings. Use the Python data type.

# 27. Write a Python program to find all the anagrams in a given list of strings and then group
# them together. Use the Python data type.

# 28. Write a Python program to find all the unique combinations of 3 numbers from a given list of
# numbers, adding up to a target number.

# 29. Write a Python program to find the third largest number from a given list of numbers.Use the
# Python set data type.
x=[4,1,2,3,5]
x.sort()
print("3rd largest third element in list: ",x[-2])


# 30. Write a Python program to remove all duplicates from a given list of strings and return a list
# of unique strings. Use the Python set data type.

x=["Mohan","Rohit","Yogesh","Govind","Mohan","Rohit","Yogesh"]

print("unique elements in the list:",set(x))

# 31. Write a Python program to find all the unique combinations of 2 numbers from a given list of
# numbers, adding up to a target number. Use the Python set data type.
        