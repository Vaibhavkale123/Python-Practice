'''
files handling in python:
file:
->they are usetd to store data permanently.
->we can data retrieve whenever we want.
->Data is stored in non-volatile memory.

types of files:
->text file
->binary file(images,audio,etc.)

file hadling means:
->reading and writing
->deleting
->creating
->copying
->moving


syntax:
file_name = open('filename','mode')


f=open("D:\Codenera\Regular\Python practice\DemoFileHandling.txt")
print(f.read())
f=open("D:\Codenera\Regular\Python practice\DemoFileHandling.txt","w+")
f.write("Hello World!")
print(f.read())
f.close()
f=open("D:\Codenera\Regular\Python practice\DemoFileHandling.txt","a")
f.write("\nThis is a new line")
f=open("D:\Codenera\Regular\Python practice\DemoFileHandling.txt")
print(f.read())
f.close()
'''
# wap to create file and add some string to it ,now read the file and find frequecy of each character.
# f.write("Hello World!")
# print(f.read())
# f.close()
# f=open("D:\Codenera\Regular\Python practice\DemoFile.txt")
# s=f.read()
# f.close()
# f={}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# for k,v in f.items():
#     print(k,"=",v)

# f=open("D:\Codenera\Regular\Python practice\DemoFile.txt","r")

# print(f.read(10))
# print(f.seek(5))
# print(f.readlines())


# wap to create a txt file and add some string,
# now read that file and find frequecy of each character.
# f=open("D:\Codenera\Regular\Python practice\DemoFile.txt","r")

# s=f.readlines()
# wap to create a txt file and add some string,
# now read that file and find the frequency of uppercase, lowercase,spaces and digit characters.
# f=open("D:\Codenera\Regular\Python practice\DemoFile.txt","r")
# f.seek(0)
# print(f.readlines())
# print(f.readlines())

# s=f.read()
# print(s)
# c_u=0
# c_l=0
# c_w=0
# c_n=0

# for i in s:
#     if i.isdigit():
#         c_n+=1
#     elif i.isspace():
#         c_w+=1
#     elif i.isupper():
#         c_u+=1
#     elif i.islower():
#         c_l+=1
# total=c_u+c_l+c_w+c_n
# print("Percentage of uppercase: ",c_u/total*100)
# print("Percentage of lowercase: ",c_l/total*100)
# print("Percentage of number: ",c_n/total*100)
# print("Percentage of spaces: ",c_w/total*100)

# Q.Write a Python program that reads
#  a list of integers from a file named numbers.txt and calculates the sum of all integers.
# f=open("D:/Codenera/Regular/Python practice/numbers.txt","r")
# nums=f.read().strip()
# nums=nums.split("\n")
# sum=0
# print(nums)
# for i in nums:
#     print(i)
#     sum+=int(i)
# print(sum)














# 2. Write a program that opens a file named "input.txt" in read mode, reads its contents,
#  and prints the number of characters in the file.
# f=open("D:/Codenera/Regular/Python practice/input.txt","r")
# s=f.read()
# f={}
# for i in s:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1

# for e,v in f.items():
#     print(f"{e},{v}")


# 3. Create a Python script that opens a text file named "numbers.txt"
#  containing numbers separated by spaces, reads them, and prints their sum.

# 4. Write a program that reads a text file named "quotes.txt" line by line 
# and prints each line preceded by its line number.
# f=open("D:/Codenera/Regular/Python practice/quotes.txt","r")
# s=f.readlines()
# c=1
# for i in s:
#     print(f"{c}. {i}")
#     c+=1







# # 5. Develop a Python script that reads a text file named "data.txt" 
# # and prints each line along with its length.
f=open("D:/Codenera/Regular/Python practice/quotes.txt","r")
s=f.read().strip().split()

for i in s:
    print(i,len(i))
    
