'''
pattern 34
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4
'''

# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end=" ")
#     c=0
#     for j in range(1,i):
#         c+=1
#         print(c,end=" ")
#     print()

'''
pattern 35
1 2 3 4 5
2 3 4 5 1
3 4 5 2 1
4 5 3 2 1
5 4 3 2 1


'''
# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end=" ")
#     c=i-1
#     for j in range(1,i):
#         print(c,end=" ")
#         c-=1

#     print()


'''
pattern 36
1 3 5 7 9
3 5 7 9 1
5 7 9 1 3
7 9 1 3 5 
9 1 3 5 7
'''
c=1
temp=1

for i in range(1,6):
    # c=1
    temp+=2
    for j in range(i,6):    
            print(c,end=" ")
            c+=2

    c=temp
    k=1
    for j in range(1,i):
        print(k,end=" ")
        k+=2

    
    print()