'''1. Write a Python program to generate the Fibonacci series up to a specified limit using a loop.
input: 7
output: 0,1,1,2,3,5,8
'''
'''
num1=0
num2=1
i=2
s=int(input("Enter range: "))
print(num1,",",num2,end=",")
while(i<=s):
    num3=num1+num2
    print(num3,end=",")
    num1=num2
    num2=num3
    i+=1

'''
'''
2. Create a program to print the multiplication table of a
given number using a loop.'''
'''
n=int(input("Enter number: "))
i=1
while(i<=10):
    print(n*i)
    
    i+=1
'''
'''

3. Wap takes a number from the user and prints its reverse no.
'''
'''
rev=0
num=int(input("Enter number: "))
i=num
rem=0
while(i!=0):
    rem=i%10
    rev=rev*10+rem
    i//=10
print(rev)
'''
'''
4. Wap takes a number from the user and checks
whether it is palindrome or not.
'''
'''

rev=0
num=int(input("Enter number: "))
i=num
rem=0
while(i!=0):
    rem=i%10
    rev=rev*10+rem
    i//=10
if(num==rev):
    print("It's palindrome")
else:
     print("It's not palindrome")
'''
    
'''
5. Wap takes a number from the user and finds the sum
and count of only an even number from it.
'''

sum=0
c=0
i=1
rem=0
n=int(input("Enter numbers of inputs: "))
while i<=n:
    num=int(input("Enter number: "))
    sum+=num
    if num%2==0:
        c+=1
    i+=1

print("Count: ",c)

print("Sum: ",sum)


