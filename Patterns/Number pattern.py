'''
Number pattern:
1. size 
2. shape
3. content

Q.
111111
222211
333111
441111
511111
'''
'''

i=1
while i<=5:
    j=i
    while j<=5:
        print(i,end="")
        j+=1
    
    j=1
    while j<=i:
        print("1",end="")
        j+=1
 
    print()
    i+=1
'''
'''
Q1
1 
22 
333
4444
55555
'''
'''

i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    
    print()
    i+=1

'''
'''
Q2
55555
4444
333
22
1
'''
'''


i=1
c=5
while i<=5:
    
    j=i
    while j<=5:
        print(c,end="")
        j+=1
    
    c-=1
    print()
    i+=1

'''
'''
Q3

5
44
333
2222
11111
'''
'''

i=1
c=5
while i<=5:
    j=1
    while j<=i:
        print(c,end="")
        j+=1
    c-=1
    print()
    i+=1
'''
'''
Q4 
11111
2222
333
22
5
'''
'''


i=1
while i<=5:
    j=i
    while j<=5:
        print(i,end="")
        j+=1
    
    print()
    i+=1
'''
'''
Q5
1
12
123
1234
12345
'''
'''

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    
    print()
    i+=1

'''
'''
Q6
12345
1234
123
12
1
'''
'''
i=1
while i<=5:
    j=i
    c=1
    while j<=5:
        print(c,end="")
        j+=1
        c+=1

    
    print()
    i+=1
'''
'''
Q7
1
21
321
4321
54321
'''
""" 
i=1
while i<=5:
    j=i
    while j>=1:
        print(j,end="")
        j-=1
    
    print()
    i+=1
 """
'''
 Q8
 54321
 4321
 321
 21
 1
 '''
'''
i=1
while i<=5:
    j=6-i
    while j>=1:
        print(j,end="")
        j-=1
        
    print()
    i+=1
 
'''
'''
Q9
1
23
345
4567
56789
'''
'''
i=1
while i<=5:
    j=1
    c=i
    while j<=i:
        print(c,end="")
        c+=1
        j+=1
    
    print()
    i+=1
'''
'''
Q10
56789
4567
345
23
1
'''
'''

i=1

while i<=5:
    j=i
    c=6-i

    while j<=5:
        print(c,end="")
        c+=1
        j+=1
    print()
    i+=1

'''
'''
Q 11
12345
2345
345
45
5
'''
'''

i=1

while i<=5:
    j=i
  
    while j<=5:
        print(j,end="")
        j+=1
    print()
    i+=1
'''
'''
Q12
5
45
345
2345
12345
'''
'''
i=1
while i<=5:
    j=1
    c=6-i
    while j<=i:
        print(c,end="")
        c+=1
        j+=1
     
    print()
    i+=1
'''
'''
Q13
5
54
543
5432
54321
'''
'''

i=1
while i<=5:
    j=1
    c=5
    while j<=i:
        print(c,end="")
        c-=1
        j+=1
     
    print()
    i+=1
'''
'''
Q14
54321
5432
543
54
5
'''
'''
i=1

while i<=5:
    j=i
    c=5
    while j<=5:
        print(c,end="")
        j+=1
        c-=1

    print()
    i+=1
'''
'''
Q15
1
123
12345
1234567
123456789
'''
'''

i=1
c=1
while i<=5:
    j=1
    
    while j<=c:
        print(j,end="")
        j+=1
    c+=2        
    print()
    i+=1
'''
Q 16
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''