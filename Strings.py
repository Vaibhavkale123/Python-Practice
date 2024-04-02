'''
Str:
It will allow insertion order.
It is immutable

a="Apple"


# reverse str
for i in range(len(a),-1,-1):
    print(a[i])

# search in str
a="Python is very good programming language"
print("good" in a)

# str slicing
a="Python is very good programming language"
print(a[2:5])
print(a[:5])
print(a[5:])
print(a[-5:-2])
# by using slicing print str in reverse order:
print(a[-1::-1])
# string function:
# upper()
# lower()
# strip(): It removes the outer spaces from the left and right.
# replace()
# capitalize(): It convert first character in uppercase
#  isUpper()
#  isLower()
#  isAlpha(): check wheter it's alphabet or not
# isalnum():check wheter it's alphanumberice  or not
# ispace()

# wap to take string from user and check it is palidrome or not

s=input("Enter String: ")
if s==s[-1::-1]:
    print("palidrome")
else:
    print("not a palidrome")



a="Python is very good programming language"
print(a.endswith("language"))
print(a.startswith("Python"))
# wap to check count of uppercase,lowercase,spaces and digit in string:

s=input("Enter String: ")

c_upper =0
c_lower =0
c_whitespace=0
c_digits=0

for i in s:
    if i.isupper():
        c_upper+=1
    elif i.islower():
        c_lower+=1
    elif i.isspace():
        c_whitespace+=1
    elif i.isdigit():
        c_digits+=1

print("lower= ",c_lower)
print("Upper= ",c_upper)
print("spaces= ",c_whitespace)
print("digits= ",c_digits)


# 1.enter a string by user and search particular element are present or not
s=input("Enter String: ")
elem=input("Enter element to search: ")
if elem in s:
    print("element is present")

else: 
    print("not present")


# 2.enter a string by user and convert it in lower case
s=input("Enter String: ")
pass(s.lower())


# 3.enter a string by user and convert it in upper case
s=input("Enter String: ")
pass(s.upper())

# 4.enter a string by user and search particular character and print its no
s=input("Enter String: ")

for i in range(len(s)):
    if s[i]=="e":
        print("index of e",i)

# 5.enter a string and count the no of vowel and consonent.
s=input("Enter String: ")
c_vowel=0
c_consonent=0
for i in s.lower():
    if i=='a':
        c_vowel+=1
    elif i=='e':
        c_vowel+=1
    elif i=='i':
        c_vowel+=1  
    elif i=='o':
        c_vowel+=1
    elif i=='u':
        c_vowel+=1      
    else:
        c_consonent+=1

print("Vowel= ",c_vowel)
print("Consonent= ",c_consonent)


# wap take a string from user and find  the occurance of 1st character.
s=input("Enter String: ")
occur=0
f=s[0]
for i in range(len(s)):
    if f in s:
        occur+=1

print("occurance of 1st character= ",occur)

# swapcase(): convert upper case to lower case and vice versa.
# title(): capitalize the first letter of each word
# split(): It break the string 

# wap to find occurance of first word:
s="Life is a long journey, but never ends. Life is short journey, but never ends."
o=0
l=s
for i in l:
    if i==l[0]:
        o+=1
print(o)

# last word occurance:

s="Life is a long journey, but never ends. Life is short journey, but never ends"
o=0
l=s.split()
print(s)
print("Last word= ",l[len(l)-1])
for i in l:
    if i==l[len(l)-1]:
        o+=1
print("Occurance= ",o)

# wap take a string from user and print only those word which is started from vowel
s="Life is beautiful"
o=0
l=s.split()
print(s)
for i in l:
    if i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u':
        print(i)


# wap take string from find the % of uppercase,lower,whitespace and numbers
s=input("Enter a String: ")
c_u=0
c_l=0
c_w=0
c_n=0

for i in s:
    if i.isdigit():
        c_n+=1
    elif i.isspace():
        c_w+=1
    elif i.isupper():
        c_u+=1
    elif i.islower():
        c_l+=1
total=c_u+c_l+c_w+c_n
print("Percentage of uppercase: ",c_u/total*100)
print("Percentage of lowercase: ",c_l/total*100)
print("Percentage of number: ",c_n/total*100)
print("Percentage of spaces: ",c_w/total*100)

# format: placeholder{}
name="Vaibhav"
age=25
city="Pune"
txt="My name is {} and I am {} years old, I belong to {}."
    
print(txt.format(name,age,city))
# f-string-> prefix f
name="Vaibhav"
age=25
city="Pune"

print(f"My name is {name} and I am {age} years old, I belong to {city}.")

# escape character: \

s="Python is good \"programming\" language."
print(s)


# frequency of each character:
s="Life is amazing."
f={}
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1

for e,v in f.items():
    print(f"{e},{v}")


'''
my_dict = {'a': 1, 'b': 2}
# my_dict.update({'b': 3})  # Adds 'c': 3
my_dict.setdefault('b', 4)  # Adds 'd': 4
print(my_dict)