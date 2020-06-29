"""
*args and **kwargs

"""
# here  a  and b are posit ional arguments
def myfunc(a,b):
    # Returns 5% of the sum of a and b
    print(sum((a,b))*0.05)
    return sum((a,b))*0.05

myfunc(40,60)

"""
here a and b are positional arguments
for multiple positonal arguments, we have to apss a tuple

"""
#
# def myfunc1(a,b,c=0,d=0,e=0):
#     # Returns 5% of the sum of a and b
#     print(sum((a,b,c,d,e))*0.05)
#     return sum((a,b,c,d,e))*0.05
#
# myfunc1(40,60,100,100,20,5)
#
# TypeError: myfunc1() takes from 2 to 5 positional arguments but 6 were given


def myfun(*args):
    print(args)

myfun(40,60,100,1,34)

def myfun(*spam):
    print(spam)

myfun(40,60,100,1,34)

#Kwargs for dicitonaries


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print ("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print ("I did not find a fruit")

myfunc(fruit='apple',veggie='lettuce')

def myfunc1(*args, **kwargs):
    print (args)
    #print (kwargs)
    print ("I would like {} {}".format(args[0],kwargs['food']))

myfunc1(10,20,30,food='eggs')

def myfu(*args):
    print (list(args))

myfu(5,6,7,8)

def func(*args):
    [print (j) for j in [(i) for i in args]]
    # for i in args:
    #     for j in i:
    #         print (j)



func('Antthor')