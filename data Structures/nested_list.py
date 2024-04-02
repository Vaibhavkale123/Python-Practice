'''
Nested lists:
Inner list
Outter list


list1=[1,2,3,4,[10,11,12],5,6,7]
print(list1)
print(list1[4][2])

list2=[1,2,3,4,[10,11,[13,14,[20,21,22],15],12],5,6,7]

print(list2[4][2][2][1])
print(list2[4][2][3])
'''

# Itterate on list:
# list1=[1,2,3,4,[10,11,12],5,6,7]
# n=len(list1)

# for i in range(n):
#     if type(list1[i]) is list:
#         if len(list1[i]) >1:
#             x=len(list1[i])
#             for j in range(x):
#                 print(i,j,list1[i][j])
#     else:
#         print(i,list1[i])


# list2=[1,2,3,4,[10,11,[13,14,[20,21,22],15],12],5,6,7]

# Iterate using for loop with index
# n=len(list2)
# for i in range(n):
#     if type(list2[i]) is list:
#         if len(list2[i])>1:
#             x=len(list2[i])
#             for j in range(x):
#                 if type(list2[i][j]) is list:
#                     if len(list2[i][j])>1:
#                         x=len(list2[i][j])
#                         for k  in range(x):
#                             if type(list2[i][j][k]) is list:
#                                 if len(list2[i][j][k])>1:
#                                     x=len(list2[i][j][k])
#                                     for l in range(x):
#                                             print(i,j,k,l,list2[i][j][k][l])
                                           
                                        
#                             else:
#                                 print(i,j,k,list2[i][j][k])
#                 else:
#                     print(i,j,list2[i][j])
#     else:
#          print(i,list2[i])

'''                
Sum of Nested List:
Write a function to find the sum of all elements in a nested list of integers.

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

Sum of all elements in the nested list: 45
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

sum=0
n=len(nested_list)
for i in range(n):
    if type(nested_list[i]) is list:
        x=len(nested_list[i])
        for j in range(x):
            sum+=nested_list[i][j]
    else:
        sum+=nested_list[i]
print(sum)



Count Occurrences in Nested List:
Write a function to count the occurrences of a given element in a nested list.
nested_list = [[1, 2, 3], [4, 2, 5], [6, 7, 8, 9], [2, 3]]
element_to_count = 2

Occurrences of 2 in the nested list: 3

'''

# def occurance(nested_list,f):
#     n=len(nested_list)
#     temp=f
#     count=1

#     for i in range(n):
#         if type(nested_list[i]) is list:
#             x=len(nested_list[i])
#             for j in range(x):
#                 if nested_list[i][j]==temp:
#                     count+=1
#         else:
#             if nested_list[i]==temp:
#                 count+=1
#         return temp

# nested_list = [[1, 2, 3], [4, 2, 5], [6, 7, 8, 9], [2, 3]]
# print("Occurrences of 2 in the nested list: ", occurance(nested_list,2))


# Q1. Wap takes the input of elements in the list and prints all palindrome no from it.
# list1=[]
# print("If you want to stop press 0")
# while(True):
#     n=int(input("Enter element:"))
#     if n==0:
#         break
#     list1.append(n)
 
# def print_palindrome(list):
#     for i in list:
#         n=i
#         rev=0
#         while(n!=0):
#             rem=n%10
#             rev=rev*10+rem
#             n//=10
#         if rev==i:
#             print(i)
# print_palindrome(list1)

# Q2. Wap takes the input of elements in the list and prints all Armstrong no from it.

# list1=[]
# print("If you want to stop press 0")
# while(True):
#     n=int(input("Enter element:"))
#     if n==0:
#         break
#     list1.append(n)

# def print_armstrong(list):
    

#     for i in list:
#         n=i
#         sum=0
#         while n!=0:
#             rem=n%10
#             sum=sum+rem*rem*rem
#             n//=10
#         if sum==i:
#             print(i)

# print_armstrong(list1)

# Q3. Wap takes the input of elements in the list and prints all prime no from it.

# list1=[]
# print("If you want to stop press 0")
# while(True):
#     n=int(input("Enter element:"))
#     if n==0:
#         break
#     list1.append(n)

# def print_primeno(list):
#     for i in list:
#         c=0
#         for j in range(2,i):
#             if i%j==0:
#                 c+=1
#         if c==0:
#             print(i)

# print_primeno(list1)

# Q4.. Write a Python function that takes a list of numbers and rotates it in the right direction, take no from yourself.

# list1=[1,57,9, 8,12 ,55]
# def rotate_list_right(list):
#     # for i in range(len(list)//2):
#     i=0
#     while i!=len(list1):
#         temp=list[i]
#         list[i]=list[i-1]
#         list[i+1]=temp
#         i+=2
    

# rotate_list_right(list1)
# print(list1)

# Q5.. Write a Python function that takes a list of numbers and rotates it in the left direction, take no from yourself.


# Q6. WAP to replace all negative value with its immediate left elements square. Means 
#      List1 = [12, 3, -19, 29, 5, -61, 44, 7, -9] 
#      Output List will be [12, 3, 9, 29, 5, 25, 44, 7, 49].

# List1 = [12, 3, -19, 29, 5, -61, 44, 7, -9] 

# def replace_all_negative_with_left_square(list):   
#     for i in range(len(list)):
#         if list[i]<0:
#             list[i]=list[i-1]*list[i-1]
#     return list

# print(replace_all_negative_with_left_square(List1))




# Q7.Wap sort half List in accending and half in decending order
#     input
#         a=[9,1,3,5,6,11,22,66,10,19].
#     output
#         a=[1,3,5,6,9,10,66,22,19,11,10]

def sort_half(list):
    print(len(list))
    n=len(list)//2-1
    print(n)
    a_list=list [:n:]
    d_list=list[n::]
    print(d_list)
    # for i in range(len(a_list)-1):
    #     if a_list[i]>a_list[i+1]:
    #         temp=a_list[i]
    #         a_list[i]=a_list[i+1]
    #         a_list[i+1]=temp

    for i in range(len(d_list)-1):
         if d_list[i]<d_list[i+1]:
            temp=d_list[i]
            d_list[i]=d_list[i+1]
            d_list[i+1]=temp
    # print("ascending list: ",a_list)
    print("descending list: ",d_list)
    
a=[9,1,3,5,6,11,22,66,10,19]
sort_half(a)
