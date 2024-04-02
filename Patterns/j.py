'''

Q6.
          A
       B A B
     C B A B C
   D C B A B C D
 E D C B A B C D E
'''
i = 1
c=1

while i <= 5:
    j = i
    while j <= 5:
        print('@', end='')
        j+= 1

    j = 1
    while j <= i:
        print(chr(64 + i-1), end='')
        j+= 1

    # j = 1
    # while j <= i:
    #     print(chr(65 + j), end=' ')
    #     j += 1
    print()
    i += 1
    c+=2
'''



Q7.
a
B c
D e F
g H i J
k L m N o
'''

'''

Q8.
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''

'''

Q9.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''


'''

Q10.

1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1 
1 2
1 2 3 
1 2 3 4 
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7


'''


# while i <= 7:
#     print(i, end=' ')
#     i += 1
# print()
# i = 1
# while i <= 6:
#     j = i
#     c=i
#     while j <= 6:
#         print(j, end=' ')

#         j+= 1
#     print()
#     i += 1
