'''
 dictionary: it will store data in key-value pairs. There are two ways to create a dictionary:
1.{}
2.dict()

properties:
1. before 3.7 unoredered, after that ordered


x={"apple":400,"mango":500,"orange":100}
print(x)
print(type(x))

# get():it will accept key as parameter and return the value 
print(x.get("apple"))
# keys(): it will return all keys in dictionary

print(x.keys())
# values(): it will return all values in dictionary

print(x.values())   
# items(): it will return key-value pairs in dictionary

print(x.items())

# how to iterate:
x={"apple":400,"mango":500,"orange":100}

# for i in x:
#     print(i)
   
# for k, v in x.items():
#     print(k, v)

for kv in x.items():
    print(kv[0],kv[1])

# how to update doctionary
x={"apple":400,"mango":200,"orange":100}
print(x)
x.update(("apple",800,"orange",500))
print(x)

# how to delete dictionary
x={"apple":400,"mango":200,"orange":100}
# del x
del x["apple"]
print(x)

# pop(): it is used delete particular items
x.pop("apple")

# popitem(): it is used to  the last item
x.popitem()


# how to delete mulitple items
x={"apple":400,"mango":200,"orange":100,"papaya":500}
print(x)

li=["apple","mango","orange"]
for i in li:
    x.pop(i)

print(x)

# how to check item is present or not:
x={"apple":400,"mango":200,"orange":100,"papaya":500}

key="apple"
if key in x.keys():
    print("item found")
else:
    print("not found")

# how to join dict
x={"apple":400,"mango":200,"orange":100,"papaya":500}
b={"blck":300,"brown":500}
x.update(b)
print(x)
# how to join multiple dict
# **kwargs
a={"apple":400,"mango":200,"orange":100,"papaya":500}
b={"black":300,"brown":500}
c={"dog":800,"cat":900}
d={**a,**b,**c}
print(d)

# copy:
# using copy() method
# using dict() function

# sort by using sorted()
x={"apple":400,"mango":200,"orange":100,"papaya":500}
print(sorted(x))
# print(sorted(x.keys()))


# dict comprehension
li=[1,2,3,4,5,6]
odd={i:i*i for i in li if i%2!=0}
print(odd)

'''

#nested dictionary

address={"State":"Punjab","city":"Mohali","pin_code":12121}
details={"name":"Amit","Company":"Codenera","Address":address}

#person details
#print(details)

#nested items

#print(details["Address"]["city"])

#iterating nested dictionary

for key,values in details.items():
    if key=="Address":
        print("printing nested data")
        for nk,nv in values.items():
            print(nk,nv)
    else:
        print(key,values)

