#print(  "hello");
'''Reverse Number'''

'''
rev=0
n=1234
i= n;
while i!=0:
    rem=i%10
    rev=rev*10+rem
    i//=10

print("original number: ",n)
print("reverse number: ", rev)
'''
''' Palidrome numbers'''

'''
rev=0
n=1213
i= n;
while i!=0:
    rem=i%10
    rev=rev*10+rem
    i//=10
if rev==n:
    print("It's palidrome number ")
else:
    print("It's not palidrome number ")
'''

'''next palidrome number'''
'''rev=0
n=24
i= n;

while rev!=n:
    i= n;
    rev=0
    while i!=0:
        rem=i%10
        rev=rev*10+rem
        i//=10
    if rev==n:
        print("It's palidrome number ")
        break
    else:
        n=n+1
        #print("It's not palidrome number ")

print("Next palidrome number is",n)'''

'''c=0
n=int(input("Enter number: "))
j=2
while(j<n):
    if n%j==0:
        c+=1
    j+=1
if c==0:
    print("It's prime number")
else:
    print("It's not a prime number")
'''
''' Factorial number'''

'''
n=int(input("Enter number: "))
i=1
fact=1;
while(i<=n):
    fact*=i
    i+=1
print("factorial of",n,"is",fact)
'''

'''fabonacci'''
'''
n1=0
n2=1
s=int(input("Enter limit for fabonacci series : "))
print(n1,n2,end=" ")
i=2
while(i<s):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    i+=1'''

#armstrong numbers
'''s=0
n=153
i= n;
while i!=0:
    rem=i%10
    s=s+rem*rem*rem
    i//=10
if s==n:
    print("It's Armstrong number ")
else:
    print("It's not Armstrong number ")
'''
#For loop
'''
for i in range(11):
    print(i)

'''
''''
1. Write a Python program to generate the
Fibonacci series up to a specified limit using a loop.
input: 7
output: 0,1,1,2,3,5,8
'''
'''
num1=0
num2=1
num=int(input("Enter number for Fibonacci series: "))
print(num1,",",num2,end=",")
for i in range(2,num):
    num3=num1+num2
    print(num3,end=",")
    num1=num2
    num2=num3

'''
'''
2. Create a program to print the
multiplication table of a given number
using a loop.
'''
'''
num=int(input("Enter number for Multiplication table: "))

for i in range(1,101):
    print(i*num)
'''
'''
3. Wap takes a number from the user and prints
its reverse no.
'''
'''
rev=0
rem=0
num=int(input("Enter number to reverse : "))
for i in range(num,-1,10):
    rem=i%10
    rev=rev*10+rem
print(rev)
'''
'''
4. Wap takes a number from the user and checks
whether it is palindrome or not.
'''
'''
5. Wap takes a number from the user and finds the sum and count of only an even number from it.
'''

'''
Q1.Display numbers from 1 to 100.
'''
'''
for i in range(101):
    print(i)

'''
'''
Q2.Display all even numbers from 1 to 100. 
'''
'''
for i in range(101):
    if i%2==0:
        print(i)
'''
'''
Q3. Write a program to print all natural numbers from 1 to n. - using for loop
'''
'''

n=int(input("Enter n to print all natural numbers from 1 to n: "))
for i in range(1,n+1):
    print(i)

'''
'''
Q4. Write a program to print all natural numbers in reverse (from n to 1). - using 
for loop

'''
'''
n=int(input("Enter n to print all natural numbers in reverse from n to 1: "))
for i in range(n,0,-1):
    print(i)
'''
'''
Q5. Write a program to print all even numbers between 1 to 100. - using while 
     loop.
'''
'''
for i in range(101):
    if i%2==0:
        print(i)
'''
'''
Q6. Write a program to print all odd number between 1 to 100.
'''
'''
for i in range(101):
    if i%2!=0:
        print(i)
'''
'''
Q7. Write a program to find sum of all natural numbers between 1 to n.
'''
'''
n=int(input("Enter n to sum of all natural numbers from 1 to n: "))

sum=0
for i in range(1,n+1):
    sum+=i

print(sum)
'''
'''
Q8. Write a program to find sum and count  of all even numbers between 1 to n.
'''
'''
n=int(input("Enter n to sum of all even natural numbers from 1 to n: "))

sum=0

for i in range(1,n+1):
    if i%2==0:
        sum+=i

print(sum)
'''
'''

Q9. Write a program to find sum  and count of all odd numbers between 1 to n.
'''
'''
n=int(input("Enter n to sum of all odd natural numbers from 1 to n: "))

sum=0

for i in range(1,n+1):
    if i%2!=0:
        sum+=i

print(sum)
'''
'''
Q10.Display all odd numbers from 200 to 300.
'''
'''
for i in range(200,301):
    if i%2!=0:
        print(i)
'''
'''

Q11.Wap enter your name and print it five times.
'''
'''
name="Vaibhav"
for i in range(6):
    print(name)
'''
'''

Q12.Wap take input first and last no and display
all odd numbers between them and find sum and count. 
'''
'''
f=int(input("Enter first no: "))

l=int(input("Enter last no: "))
sum=0
c=0
for i in range(f,l+1):
    if i%2!=0:
        sum+=i
        c+=1
print("sum",sum)
print("count",c)


'''
'''
Q13.Wap take input first and last no and display all even numbers between them and find sum and find sum an count.

'''
'''
f=int(input("Enter first no: "))

l=int(input("Enter last no: "))
sum=0

c=0
for i in range(f,l+1):
    if i%2==0:
        sum+=i
        c+=1
print("sum",sum)
print("count",c)
'''
'''

Q14..WAP to add multiple  number, ask user to take  input as their need. 
   press 0 to terminate inputting after that calculate sum of that inputted number.
'''

'''
l=int(input("Enter last no: "))
sum=0

c=0
for i in range(f,l+1):
    if i%2==0:
        sum+=i
        c+=1
print("sum",sum)
print("count",c)

'''
 
'''
Q15.Wap to take input a no and print table.

'''
#reverse number using for loop
'''
num=1234
n1=num
n=len(str(n1))
rev=0
for i in range(n):
    rem=n1%10
    rev=rev*10+rem
    n1//=10
print("original no. ",num)
print("reverse no. ",rev)
'''
'''
Q1. Wap takes a number from the user and prints its reverse number using for loop.

Q2. Wap takes a number from the user and checks whether it is palindrome or not using for loop.
'''

'''
num=1234
n1=num
n=len(str(n1))
rev=0
for i in range(n):
    rem=n1%10
    rev=rev*10+rem
    n1//=10
if(num==rev):
    print("palindrome no. ",num)
else:
    print("not a palindrome no. ",rev)
 
'''
'''
Q3.  Wap takes a number from the user and checks whether it is Armstrong or not using for loop.
'''
'''
#Armstrong no

num=153
n1=num
n=len(str(n1))
rev=0
for i in range(n):
    rem=n1%10
    rev=rev+rem*rem*rem
    n1//=10
if(num==rev):
    print("Armstrong no. ",num)
else:
    print("not a Armstrong no. ",rev)
''' 
'''
Q4.  Wap takes a number from the user and
checks whether it is Prime or not using
for loop.
'''
'''
num=int(input("Enter any number: "))
c=0
for i in range(2,num):
    if(num%i==0):
        c+=1
    
if(c==0):
    print("Prime no. ",num)
else:
    print("not a Prime no. ",num)
'''
'''

Q5.  Wap take a number from the user and
prints the Fabonascii series using a for loop.
'''
'''
#Fabonascii series
n1=0
n2=1
num=int(input("Enter range for Fabonascii series: "))

print(n1," ",n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
'''
'''
Q.Automorphic numbers, also known as circular numbers,
are numbers whose square ends with the same digits as the number itself.
For example, 5 is an automorphic number since 5^2 = 25,
and 25 ends with the same digit as 5. Similarly, 76 is an automorphic

number as 76^2 = 5776.

To determine if a number is an Automorphic Number in Python, follow these steps:

1. Accept the number from the user.
2. Calculate the square of the number.
3. Extract the last n digits of the square, where n is the number of digits in the original number.
4. Compare the extracted digits with the original number to check if they are the same.

Write a Python program to implement the above steps and determine if a given number is an Automorphic Number or not.
'''
'''
num=76
n1=len(str(num))
s=num*num
n=len(str(s))
n2=s
rev=0

for i in range(n1): 
    rem=n2%10 
    rev=rev*10+rem  
    n2//=10

rev1=0
for i in range(n1):
    rem=rev%10 
    rev1=rev1*10+rem
    rev//=10
    
if(num==rev1):
    print("Automorphic no. ",rev1)
else:
    print("not a Automorphic no. ",rev1)

'''
'''
Q.Neon numbers are numbers where the sum of the digits of the square of the number equals the number itself. For example,
9 is a neon number because 9^2 = 81, and the sum of the digits of 81 (i.e., 8 + 1) equals 9.

To determine if a number is a Neon Number in Python, follow these steps:

1. Accept the number from the user.
2. Calculate the square of the number.
3. Sum the digits of the square.
4. Compare the sum with the original number.

Write a Python program to implement the above steps and determine if a given number is a Neon Number or not.
'''
'''
num=3
n1=len(str(num))
s=num*num
n=len(str(s))
n2=s
rev=0

for i in range(n): 
    rem=n2%10 
    rev=rev+rem  
    n2//=10

    
if(num==rev):
    print("Neon no. ",rev)
else:
    print("not a Neon no. ",rev)
'''
#nested loop:
#palindrome from 10 to 200
'''
j=10
while(j<=200):
    i=j
    rem=0
    rev=0
    while(i!=0):
        rem=i%10
        rev=rev*10+rem
        i//=10
    if(rev==j):
        print(rev)
    j+=1
'''
#prime numbers
'''
j=1
while(j<=200):
    i=2
    c=0
    while(i<j):
        if(j%i==0):
            c+=1
        i+=1
    if(c==0):
        print(j)
    j+=1
'''
#Q1. Wap take a last number from user
#and print all palindrome no between them.
'''
l=int(input("Enter last no. to print all palidrome no. from 1 to last no: "))

for i in range(10,l):
    n=i
    n1=len(str(i))
    rem=0
    rev=0
    
    for j in range(n1):
        rem=n%10
        rev=rev*10+rem
        n//=10

    
    if(rev==i):
        print(rev)
    

'''
'''
Q2. Wap take a last number from user and print all
Armstrong no between them.
'''
'''

l=int(input("Enter last no. to print all armstrong no. from 1 to last no: "))

for i in range(1,l):
    n=i
    n1=len(str(i))
    rem=0
    rev=0
    
    for j in range(n1):
        rem=n%10
        rev=rev+rem*rem*rem
        n//=10

    
    if(rev==i):
        print(rev)
'''
'''
Q3. Wap take a last number from user and
print all prime no between them.j=10

'''
'''
l=int(input("Enter last no. to print all prime no. from 1 to last no: "))

for i in range(2,l):
    
    c=0
    for j in range(2,i):
        if(i%j==0):
            c+=1

    
    if(c==0):
        print(i)
'''
'''
Q1.Factorial Calculation: Write a program to
calculate the factorial of a given number
using a "for" loop.
'''
'''
n=5
fact=1
for i in range(1,n+1):
    fact*=i

print(fact)
'''
'''
Q2.Prime Number Check: Create a program that
takes a number as input and determines whether
it's a prime number or not using a "for" loop.
'''
'''
n=int(input("Enter no.: "))
c=0
for i in range(2,n):
    if n%i==0:
      c+=1
if(c==0):
      print("prime no")
else:
    print("not a prime no")
'''
'''
Q3.Multiplication Table: Generate the multiplication table for a given number using a "for" loop. Display the table from 1 to 10.
'''
'''
num=int(input("Enter number for Multiplication table: "))

for i in range(1,11):
    print(i*num)
'''
'''
Q4.Fibonacci Sequence: Write a program to print
the first N numbers of the Fibonacci sequence using a "while" loop.
'''
'''
num1=0
num2=1
num=int(input("Enter number for Fibonacci series: "))
print(num1," ",num2,end=" ")
for i in range(2,num):
    num3=num1+num2
    print(num3,end=" ")
    num1=num2
    num2=num3

'''
'''
Q5.Sum of Digits: Create a program that
calculates the sum of the digits of a given number
using a "while" loop.
'''
'''
n=int(input("Enter  no. to print sum of the digits: "))
i=n
rem=0
sum=0
while(i!=0):
    rem=i%10
    sum+=rem
    i//=10
print(sum)
'''
'''
Q6.Palindrome Check: Develop a program that
checks whether a given string is a palindrome or not using a "for" loop.
'''
s=input("Enter string: ")
l=len(s)
r=""
print(s[1])
for i in range(l,0,-1):
    r=r+s.index(i)
if r==s:
    print("palindrome")
else:
    print("not a palindrome")

    
'''
Q7.Power Calculation: Write a program to calculate the power of a number raised to an exponent using a "for" loop.
'''
