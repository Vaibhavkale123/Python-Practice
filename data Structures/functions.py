'''
Create Menu program in Python for following mathematical operations 
1.Addition
2.Substraction
3.Multiplication
4.Division
5.Exit
ask user to choose any Number from above menu to perform operations.
'''
def addition():
  a=int(input("enter 1st no: "))
  b=int(input("enter 2nd no: "))
  c=int(input("enter 3rd no: "))
  d=a+b+c
  print(d)

def substraction():
  a=int(input("enter 1st no: "))
  b=int(input("enter 2nd no: "))
  c=int(input("enter 3rd no: "))
  d=a-b-c
  print(d)


def multiplication():
  a=int(input("enter 1st no: "))
  b=int(input("enter 2nd no: "))
  c=int(input("enter 3rd no: "))
  d=a*b*c
  print(d)

def division():
  a=int(input("enter 1st no: "))
  b=int(input("enter 2nd no: "))
  c=int(input("enter 3rd no: "))
  d=a/b/c
  print(d)  

# print("---Menu----")
# print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
# c=int(input("enter your choice: "))
# if c==1:
#     addition()
# elif c==2:
#     substraction()
# elif c==3:
#     multiplication()
# elif c==4:
#     division()
# else:
#     print("exit")


# Q1. Wap takes any no from the user and print their Fabnascii series using function.

def fabnascii():
    n1=0
    n2=1
    n=int(input("enter any no: "))
    print(n1,n2,end=" ")
    i=2
    while i<=n:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        i+=1

# fabnascii()

# Q2. Wap take input of 5 digit no and print sum and 
# count of only even no using function.
def evenSumDigits():
    s=0
    num=int(input("enter any 5 digit no: "))
    n=num
    while n!=0:
        rem=n%10
        if rem%2==0:
            s+=rem
        n//=10
    print(s)        
# evenSumDigits()

# Q3. Wap take input of 5 digit no and print sum and 
# count of only odd no using function.

def oddSumDigits():
    s=0
    num=int(input("enter any 5 digit no: "))
    n=num
    while n!=0:
        rem=n%10
        if rem%2!=0:
            s+=rem
        n//=10
    print(s)        
# oddSumDigits()

# fact nos
def fact():
    fact=1
    n=int(input("enter any no: "))
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
# fact() 

# Q1. Wap takes 1st and last no as an argument in function 
# and prints all palindrome no.
def palindrome(f,l):
    i=f
    while(i<=l):
        n=i
        rev=0
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n//=10
        if rev==i:
            print(rev)
        i+=1
# palindrome(1,100)
# palindrome(100,200)

# Q2. Wap takes 1st and last no as an argument in function and prints all armstrong no.
def armstrong(f,l):
    i=f
    while(i<=l):
        n=i
        rev=0
        while n!=0:
            rem=n%10
            rev=rev+rem**3
            n//=10
        if rev==i:
            print(rev)
        i+=1

# armstrong(1,200)

# Q3. Wap takes 1st and last no as an argument in function and prints all prime no.
def prime(f,l):
    i=f
    while (i<=l):
        j=2
        c=0
        while(j<i):
            if (i%j==0):
                c+=1
            j+=1
        
        if c==0:
            print(i)
        i+=1
# prime(10,100)
# Q4. Wap takes any no from the user and returns their factorial.

def fact(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
# n=int(input("enter any no: "))

# fact(n) 

# Q5. Wap takes any no from the user and print their Fabnascii series.     


def fabnascii(n):
    n1=0
    n2=1
    print(n1,n2,end=" ")
    i=2
    while i<n:
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
        i+=1

n=int(input("enter any no: "))

fabnascii(n)