"""
One time use funcitons , anonymous functions

map-0 Mapping elements

"""

def Square(num):
    return num**2

mu_nums=[1,2,3,4,5]

map(Square,mu_nums)

print (map(Square,mu_nums))

for i in map(Square,mu_nums):
    print (i)

print(list(map(Square,mu_nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        return "EVEN"
    else:
        return mystring[0]

names=["Sammy", "JAMe","Andy"]

print (tuple(map(splicer, names)))


def check_even(num1):
    return num1%2==0

mynums=[1,2,3,4,5,6]

print(list(filter(check_even,mynums)))

def square(num):
    result=num**2
    return result

print (square(3))

def square(num):
    return num**2

print (square(4))

def square(num): return num**2

print (square(4))

square= lambda num: num**2

print (square(5))

print (list(map(lambda num: num**2,mu_nums)))

print (list(filter(lambda num: num%2==0,mu_nums)))

