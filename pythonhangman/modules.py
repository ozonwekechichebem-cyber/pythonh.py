import datetime
x = datetime.datetime.now()
print(x)

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

import datetime
x = datetime.datetime(2025, 10, 8)
print(x)

import datetime
x = datetime.datetime(2025,10,8)
print(x.strftime("%B"))

import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))

import datetime
x = datetime.datetime.now()
print(x.strftime("%x"))

x = min(5, 10, 25)
y = max(5,10,25)
print(x)
print(y)

x = abs(-7.25)
print(x)

x =pow(4,3)
print(x)

import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

import math

x = math.pi
print(x)

# to remove duplicates from list
mylist = ["a","b","c","c"]
mylist = (dict.fromkeys(mylist))
print(mylist)

#to reverse a strinng in python
-1
txt = "hello world"[::-1]
print(txt)

def my_function(x):
    return x[::-1]
    mytxt = my_function("I wonder how this text looks like backwards")
    print(mytxt)

#membership in range
r = range(0,10,2)
print(6 in r)
print(7 in r)

#lenght in range
r = range(0,10,2)
print(len(r))