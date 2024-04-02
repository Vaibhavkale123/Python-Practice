from calc import Calculator


class Impl(Calculator):
    def addition(self) :
        a=int(input("enter 1st no: "))
        b=int(input("enter 2nd no: "))
        print("result of addition =",a+b)

    def subtraction(self) :
        a=int(input("enter 1st no: "))
        b=int(input("enter 2nd no: "))
        print("result of subtraction =",(a-b))

    def multiplication(self) :
        a=int(input("enter 1st no: "))
        b=int(input("enter 2nd no: "))
        print("result of multiplication =",(a*b))

    def division(self) :
        a=int(input("enter 1st no: "))
        b=int(input("enter 2nd no: "))
        print("result of division =",(a/b))



