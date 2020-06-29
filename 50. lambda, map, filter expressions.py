def square(num):
    print (num**2)

muy_nums=[1,2,3,4,5]

print(map(square,muy_nums))

"""
mapping every single element to the functions
"""

def square(num):
     return (num**2)

muy_nums=[1,2,3,4,5]

for i in map(square,muy_nums):
    print (i)

def splicer(mystr):
    if len(mystr)%2==0:
        return "EVEN"
    else:
        return mystr[0]

names=["andy","steve","Sally"]

print(list(map(splicer,names)))

 ## Returns True or not if true it comes

def check_even(num):
     return num%2==0

my_nums=[1,2,3,4,5,6]

print (filter(check_even,my_nums))

print (list(filter(check_even,my_nums)))

for n in filter(check_even,my_nums):
    print (n)


###lambda

def sqr(num):
    result=num**2
    print (result)

sqr(3)


def sqr(num):
    print (num**2)

sqr(4)


def sqr(num): print (num**2)

sqr(5)

square= lambda num: num**2

print (square(5))

#lamnbda with map

print (list(map (lambda num:num**2,my_nums)))

#lambnda with filter

print (list(filter(lambda  num:num%2==0,my_nums)))

print(list(map(lambda x:x[0],names)))