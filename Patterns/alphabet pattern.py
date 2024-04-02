'''
type casting: one type into another type:
there are two type in Python:
implicit conversion
explicit conversion

str()
chr()


ascii values:
a=97
A=65



Q1.
A
B B
C C C
D D D D
E E E E E
'''
'''

k=65
i=1
while(i<=5):
    j=1
    while(j<=i):
        print(chr(k), end="")
        j+=1
    k+=1
    print()
    i+=1
'''

'''
Q2.
E
D D
C C C
B B B B
A A A A A
'''
'''

k=69
i=1
while(i<=5):
    j=1

    while(j<=i):
        print(chr(k), end=" ")
        j+=1
    k-=1
    print()
    i+=1

'''

'''


Q3.
A
A B
A B C
A B C D
A B C D E

'''
'''

i=1
while(i<=5):
    j=1
    k=65

    while(j<=i):
        print(chr(k), end=" ")
        j+=1
        k+=1

    print()
    i+=1
'''


'''

Q4.
A
B A
C B A
D C B A
E D C B A

'''
'''

i=1
k=64

while(i<=5):
    j=1
    k=k+i
    while(j<=i):
        print(chr(k), end=" ")
        j+=1
        k-=1

    print()
    i+=1



'''
'''

Q5.
A
B C
C D E
D E F G
E F G H I

'''
'''

i=1
k=64

while(i<=5):
    j=1
    k=k+i
    while(j<=i):
        print(chr(k), end=" ")
        j+=1
        k+=1
    k=64
    print()
    i+=1


'''
'''

Q6.
A B C D E
B C D E
C D E
D E
E
'''
'''

i=1
k=64
while(i<=5):
    j=i
    k=k+i
    while(j<=5):
        print(chr(k), end=" ")
        j+=1
        k+=1
    k=64
    print()
    i+=1

'''
'''

Q7.
E
E D
E D C
E D C B
E D C B A

'''
'''
i=1

while(i<=5):
    j=1
    k=69
    while(j<=i):
        print(chr(k), end=" ")
        j+=1
        k-=1
    print()
    i+=1

'''
'''

Q8.
A
A B C
A B C D E
A B C D E F G
A B C D E F G H I
'''
'''

i=1
c=1
while(i<=5):
    j=1
    k=65
    while(j<=c):
        print(chr(k), end=" ")
        j+=1
        k+=1
    c+=2
    print()
    i+=1

'''

'''

Q8.
E E E E E
D D D D
C C C
B B
A
'''
'''



i=1
k=69

while(i<=5):
    j=i
    while(j<=5):
        print(chr(k), end=" ")
        j+=1
    k-=1
    print()
    i+=1


'''
'''


Q9.
A A A A A
B B B B
C C C
D D
E
'''
'''

i=1
k=65

while(i<=5):
    j=i
    while(j<=5):
        print(chr(k), end=" ")
        j+=1
    k+=1
    print()
    i+=1

'''
'''

Q10.
A B C D E
A B C D
A B C
A B
A
'''
'''


i=1
while(i<=5):
    k=65
    j=i
    while(j<=5):
        print(chr(k), end=" ")
        j+=1
        k+=1

    print()
    i+=1
'''

#Hollow pattern
'''
*****
*   *
*   *
*   *
*****



i=1
while i<=5:
    j=1
    while(j<=5):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1



*
**
* *
*  *
*****



i=1
while i<=5:
    j=1
    while(j<=i):
        if j==1 or j==i or i==5 :
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1



*****
*  *
* *
**
*


i=1
while i<=5:
    j=1
    while j<=5:
        if i==1 or j==i or j==5 :
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1



     * 
    * * 
   *   * 
  *     * 
 * * * * * 
'''



i=1
while i<=5:
    j=i
    while j<=5:
        print(" ",end="")
        j+=1
    j=1
    while j<=i:
        if i==5 or j==i or j==1 :
            print("* ",end="")
        else:
            print("  ",end="")

        j+=1
    print()
    i+=1


