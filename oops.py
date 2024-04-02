'''
oops: object oriented programming system


method: function is known method in class and object concepts but the diff is it should have self variable in first argument
 and it'smandatory

 self variable: It is the memory referene variable that holds the value from the object

# palindrome:

class A:
    def palindrome(self,num):
        n=num
        rev=0
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n//=10
        if num==rev:
            print("it's palindrome")
        else:
            print("it's not palindrome")
obj_A=A()
obj_A.palindrome(121)
obj_A.palindrome(123)


# armstrong


class P:
    def palindrome(self,num):
        n=num
        rev=0
        while n!=0:
            rem=n%10
            rev=rev+rem**3
            n//=10
        if num==rev:
            print("it's armstrong number")
        else:
            print("it's not armstrong number")
obj_A=P()
obj_A.palindrome(121)
obj_A.palindrome(153)


#  prime no

class P:
    def prime_nos(self,num):
        n=num
        for i in range(2,n+1):
            for j in range(2,i):
                if  i%j==0:
                 break
                
            else:
                print(i)
obj_A=P()
obj_A.prime_nos(100)


#  factorial no

class F:
    def fact_nos(self,num):
        fact=1
        for i in range(1,num+1):
            fact*=i
        print(fact)
            
obj_f=F()
obj_f.fact_nos(5)


# reverse no:

class R:
    def reverse_num(self,num):
        print("original no: ",num)
        n=num
        rev=0
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n//=10
        print("reverse number: ",rev)
obj_A=R()
obj_A.reverse_num(1234)

#types of methods:
1. no return no arg
2.
3.
4.

# wap to take no from user and check it's palindrome or not. if palindrome return true else false


class Calcualtion:
    def palindrome(self,num):
        n=num
        rev=0
        while n!=0:
            rem=n%10
            rev=rev*10+rem
            n//=10
        if num==rev:
            return True
        else:
            return False
obj_p=Calcualtion()
print(obj_p.palindrome(121))
print(obj_p.palindrome(123))

# constructor: 
- It is special type of method that autoamatically constructor
- it is used to initialize object
- by default value of object is null

# how to create constructor:
- def __init__(self)

# type of constructor
1. default construtor (obj null)
2. parameterized constructor
3. non parmaeterized constructor






# Q1. Wap to print all palindrome no from list , using constructor

class Palidrome:
    def __init__(self,num):
        for i in num:
            n=i
            rev=0
            while n!=0:
                rem=n%10
                rev=rev*10+rem
                n//=10
            if i==rev:
                print(i)
            
li=[1,22,3,42,121,44,25,64,77,48]
obj_p=Palidrome(li)


# Q2. Wap to print all prime no from list , using constructor


class Prime_no:
    def __init__(self,num):
        for i in num:
            for j in range (2,i):
                if i%j==0:
                    break
            else:
                print(i)


            
li=[11,22,3,42,121,44,25,64,77,48]
obj_p=Prime_no(li)






# Q3. Wap to print all Armstrong no from list , using constructor

class Armstrong:
    def __init__(self,num):
        for i in num:
            n=i
            rev=0
            while n!=0:
                rem=n%10
                rev=rev+rem*rem*rem
                n//=10
            if i==rev:
                print(i)
            
li=[1,22,3,42,121,44,25,64,77,153,48]
obj_p=Armstrong(li)

Inheritance: It is the process in which child class aquire the behiviour and property of parent class

types:
1. Single level inheritance
2. Multilevel inheritabnce
3. Multiple inheritance (A,B->C)
4. Hierachical inheritance (A->B,C,D)

Q1. wap to print min from child class and max from parent class

class P():
    def max(self,list):
        return max(list)
    
class C(P):
    def min(self,list):
        return min(list)
li=[1,2,3,4,5,6,7,8]
obj=C()
print(obj.min(li))
print(obj.max(li))



# 1. Single level inheritance

class A:
    def disp(self):
        print("I am parent 1")

class B(A):
    def disp1(self):
        print("I am parent 2")

ob=B()
ob.disp()
ob.disp1()        





2. Multilevel inheritabnce
class A:
    def disp(self):
        print("I am parent 1")

class B(A):
    def disp1(self):
        print("I am parent 2")
class C(A):
    def disp2(self):
        print("I am parent 3")

ob=C()
ob.disp()
ob.disp1()        
ob.disp2()        









# 4. Hierachical inheritance (A->B,C,D)
class A:
    def disp(self):
        print("I am parent 1")

class B(A):
    def disp1(self):
        print("I am parent 2")
class C(A):
    def disp2(self):
        print("I am parent 3")
class D(A):
    def disp3(self):
        print("I am parent 4")
ob=D()
ob.disp()
ob.disp3()        

# 5. Hybrid Inheritance (A->B,c->D ) (aka Diamond problem)

class A:
    def disp(self):
        print("I am parent 1")

class B(A):
    def disp1(self):
        print("I am parent 2")
class C(A):
    def disp2(self):
        print("I am parent 3")
class D(B,C):
    def disp3(self):
        print("I am parent 4")
ob=D()
ob.disp()
ob.disp1()
ob.disp2()
ob.disp3()        



Access specifier:

class A:
    a=99

    def __init__(self,id, name):
        self.id = id
        self.name = name

    def disp(self):
        print("disp called")
        print(self.id)
        print(self.name)
        print("disp call end")


ob=A(5,"xyz")
# print(A.a) # static/ class variable
ob.disp()


types of method:
1. Instance method: A method which pass self variable as a first argument.

2. Class method : It is used to access class variable, we can pass cls or any variable and use @Classmethod decorator.

3. Static method:
# class A:
#     a=99

#     def __init__(self,id, name):#instance method
#         self.id = id
#         self.name = name

#     @classmethod
#     def disp(cls):      
#         # print(cls.id) #this throw error as this is class method , you can access only static variable here
#         # print(cls.name)        
#         print(cls.a)

       
#     @staticmethod
#     def output():
#         print("output")

# A.output()
# ob=A(5,"xyz")
# ob.disp()
# ob.output()

# experiment:
class A:
    a=100
    def __init__(self,a):#instance method
        self.a = a
       
    def output(self):
        print(self.a,a)

# A.output()
ob=A(5)
ob.output()

# Decorators:It is used to modify the another function that already declared

# creation of decorator:

def smart(func):
    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner

@smart
def div(a,b):
    return a/b

print(div(2,8))


# access modifier:
1. public/default: It will accessible from everywhere
2. protected: It will only accessible only in inherited area (we can create is using '_')(also accesible outside of inheritance)
3. private:It will only accessible only in same area (we can create is using '__')(also accesible outside of inher


# public
class A:
    a=10


ob=A()
print(ob.a)


# protected
class A:
    _a=10

class B(A):
    b=5

ob=B()
print(ob._a)


#private
class A:
    __a=10


ob=A()
# print(ob.__a)

# name mangling:by using this process we can access private member outside of class
print(dir(ob))
print(ob._A__a)

# polymorphism
1. must have atleast 2 classes
2. must have same method between them
3. Inheritance
 


class A:
    def disp(self):
        print("I am A")
    

class B(A):
    def disp(self):
        super().disp()
        print("I am B")


ob=B()
ob.disp()


#  python does not support method overloading but support method operating:
print(110+220)
print("110"+"220")


# magic methods: generlly used for perfoming operation with object:
# ex: __add__



# without magic method:
class Book:
    def __init__(self,page):
        self.page=page
    
ob=Book(100)
ob1=Book(200)
print(ob+ob1)

# with magic method:
class Book:
    def __init__(self,page):
        self.page=page
    
    def __add__( self,other ):
        return self.page +other.page
ob=Book(100)
ob1=Book(200)
print(ob+ob1)      


'''
# Abstraction: It is the process in which we hide the internal implementation 
# of program and showing only funnctionality

# Abstract method:It is type of method in which only declaration is there