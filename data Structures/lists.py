#10,20,30,40,50

# Fetching the items from index
# list1= [10,20,30,40,50,60] #homogeneous
# list2=[10,10,"hello",30.45,40,True,60] #heterogeneous


# print(list2[5])
# print(list2[-4])

# print(list1)
# print(list2)

# properties of list:
# mutable: can be change/update
# duplicate
# oredered
# heterogeneous

# list2=[10,10,"hello",30.45,40,True,60] #heterogeneous

# for i in list2:
#     print(i,end=" ")



# WAP to print all the even number from List
# list1=[10,20,18,4,17,13,22,4,5]

# for i in list1:
#     if i%2==0:
#         print(i,end=" ")

#WAP to print all the odd numbers from list 
# list1=[10,20,18,4,17,13,22,4,5]

# for i in list1:
#     if i%2!=0:
#         print(i,end=" ")

#WAP to print all the numbers from list that is greater than 30
# list1=[10,200,138,44,17,13,22,34,5]

# for i in list1:
#     if i>30:
#         print(i,end=" ")


#WAP to print all the positive number from list. 
# list1=[10,200,-138,-44,17,-13,0,0.22,34,-5]

# for i in list1:
#     if i>=0:
#         print(i,end=" ")

#WAP to print all the negative number from list.

# list1=[10,200,-138,-44,17,-13,0,0.22,34,-5]

# for i in list1:
#     if i<0:
#         print(i,end=" ")


# Slicing in list: Extract the portion of list
# list1=[1,2,3,4,5,6,7,8,9,10]


# syntax: List[start: step: stop]
# stop: n-1

# print(list1[1:5]) #1-4
# print(list1[:4])  #0-3

# print(list1[-1:-5:-1])  #0-3

# # reverse the list
# print(list1[::-1])  #0-3


# to print index with list:
# list1=[1,2,3,4,5,6,7,8,9,10]

# for i in range(len(list1)):
#     print(i,'->',list1[i])

# Adding element in the list:
# Append()

# list1=[1,2,3,4,5,6,7,8,9,10]
# print("original list ",list1)
# list1.append("hello")
# print("after adding element ",list1)

# adding item at specific position
# insert(index, object or item)
# list2=[10,20,30,40,50]
# print(list2)
# list2.insert(2,90)
# print(list2)


# adding multiple item in single list
# using extend()
# list3=[10,20,30,40,50]

# list3.extend((90,100,120))
# print(list3)


# even list:
# list1=[10,20,30,40,50]
# evenlist=[]
# for i in list1:
#     if i%2==0:
#         evenlist.append(i)


#WAP to print all the palindrom items from list 
#  list1=[121,11,23,34]
#  output: 121,11

# list1=[121,11,23,34]
# for i in list1:
#     rev=0
#     n=i
#     while(n!=0):
#         rem=n%10
#         rev=rev*10+rem
#         n//=10
#     if i==rev:
#         print(rev)


# modifying list using slicing
# list1=[1,2,3,4,5,6]
# list1[1]=90
# print(list1)
# list1[3:5]=[60,70]
# print(list1)
# list1[3:]=[6,7]
# print(list1)


# list1=[1,2,3,4,5,6]
# for i in range(len(list1)):
#     square=list1[i]*list1[i]
#     list1[i]=square
# print(list1)

# Removing item from list:
# single item
# list1=[1,2,3,4,5,6]

# list1.remove(4)
# print(list1)
# list1.remove(2)
# print(list1)


# # multiple items
# list2=[1,2,3,2,5,6,2]

# for i in list2:
#     if i==2:
#         list2.remove(i)
# print(list2)


'''
 pop item:
 It remove items by index
 
'''
# list1=[1,2,3,4,5,6,]
# list1.pop(1)
# print(list1)


# clear
# list1=[1,2,3,4,5,6,]
# list1.clear()
# print(list1)

# del
# list1=[1,2,3,4,5,6]
# # del list1
# print(list1)
# del list1[2:4]
# print(list1)


# list2=[10,20,30,40,50,60]
# print(list2.index(4))
# list3=[1,2,3,4,5,6]

# list3.remove(60)  #x not in list
# list3.pop(6)


list1=[1,2,3,4,5,6]

list2=[10,20,30,40,50,60]


# concatation using + operator:
# list3=list1+list2
# print(list3)


# concatation using extend():
# list1.extend(list2)
# print(list1)


# copy in list:
'''
1. Deep copy:
-use =
-if change copied value it will reflect in original value

2. Shallow copy:
- use 'copy()'
-doesn't affect on original value of any changes in copied list
'''
# Shallow copy:

# list3=[1,2,3,4,5,6]
# list4=list3.copy()
# list4.append(20)
# print(list4)
# print(list3)

# deep copy
# list5=[1,2,3,4,5,6]
# list6=list5
# list6.append(50)
# print(list6)
# print(list5)



# sort():
# list1=[2,5,8,3,4,1,6,7]
# list1.sort()
# print(list1)
# # reverse()
# list1.reverse()
# print(list1)
# # max() and min()
# print(max(list1))
# print(min(list1))

# # sum()
# print(sum(list1))

# passing list in function

'''
def findMax(list):
    return max(list)

list1=[10,20,30,40 ,50]
print(findMax(list1))
'''



'''
1. Sum of List Elements:
   Write a Python function that takes a list of numbers as input and returns the sum of all the numbers in the list.

def sumOfList(list):
    return sum(list)

list1=[10,20,30,45,60]
print(sumOfList(list1))


   





2. Find Maximum in List:
   Write a Python function that finds and returns the maximum value in a list of numbers without using the max() function.

def findMax(list):
    max=0
    for i in list:
        if max<i:
            max=i
    return max 


list1=[10,25,30,40 ,50]
max_num=findMax(list1)
print(max_num)



3. List Reversal:
   Write a Python function to reverse a list in-place. Do not use any built-in list reversal functions.


def reversal(list):
    return list[::-1]

list1=[10,25,30,40 ,50]

print(reversal(list1))






4. Count Occurrences:
   Write a Python function that takes a list and a value as input and returns the number of times the value appears in the list.
def findOccuranceOfElement(list,n):
    count=0
    for i in list:
        if i==n:
            count+=1
    return(count)


list1=[10,25,50,30,40,30 ,50]

print(findOccuranceOfElement(list1,50))




5. Remove Duplicates:
   Write a Python function that takes a list as input and returns a new list with duplicate elements removed while preserving the original order of elements.
'''
# def removeDuplicates(list):
#     # list.sort()
#     for i in range(len(list)):
#         for j in range(i+1,len(list)):
#             if list[i]==list[j]:
#                 list.pop(j)
        
#     return list

# list1=[10,25,50,30,40,30 ,50]

# print(removeDuplicates(list1))




'''

8. Function to Filter Odd Numbers:
   Write a Python function that takes a list of numbers and returns a new list containing only the odd numbers from the original list.


9. List Sum of Even and Odd:
Write a Python function that takes a list of numbers and returns a tuple containing the sum of even and odd numbers separately.

10. WAP to find 2nd max element from list 

11. WAP to find the 3rd min element from list

12. WAP to find the 2nd min element from list
'''




# list comprehension
'''
x=[1,2,3,4,5,6,7,8,9,10]
even=[i for i in x if i%2==0]
print(even)

even=[i**2 for i in x if i%2==0]
print(even)

Q1.Filtering even numbers: Write a Python program that takes a list of integers and returns 
a new list containing only the even numbers using list comprehension.
'''

# x=[1,2,3,4,5,6,7,8,9,10]
# even=[i for i in x if i%2==0]
# print(even)

'''
Q2.Cube values: Create a Python program that generates a list of cube 
of numbers from 1 to 10 using list comprehension.


'''
# x=[1,2,3,4,5,6,7,8,9,10]
# even=[i**3 for i in x ]
# print(even)


