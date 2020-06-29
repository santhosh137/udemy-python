"""
Many objects in python are itreable meaning we can iterate over every element in the object
such as every element in a list or every character in a string.

we can use for loop s to execute a block of code for every iterations

The term iterable means you can iterate over the object

For example you can iterate over every  character in astring , every item in list,
every key in a dictionary

"""

#Syntax for loop

my_iterable=[0,1,2,3]

for item in my_iterable:
    print(item)

for item in my_iterable:
    print(item,end=" ")

for i in range(10):
    print (i)

for i in range(10):
    if i%2==0:
        print ("even number",i)
    else:
        print ("odd number",i)

li=[0,1,2,3,4,5,6,7,8,9,10]

list_sum=0

for i in li:
    list_sum=i+list_sum
    print(list_sum)

print ("\n")
print(list_sum)

mystring="JHello World"

for alpha in mystring:
    print (alpha)

for _ in mystring:
    print(_,end=" ")

tup=(1,2,3,3,4)

for _ in tup:
    print(_)

my_list=[(1,2),(3,4),(5,6),(7,8)]

for i in my_list:
    print (i)

for (a,b) in my_list:
    print(a)
    print (b)

for (a,b) in my_list:
    print(a)

l1=[(1,2,3),(5,6,7),(8,9,0)]

for (a,b,c) in l1:
    print (a)

d={'k1': 1, 'k2':2,'k3':3}

for i in d:
    print (i)

for i in d.items():
    print(i)

for key,value in d.items():
    print (value)

for value in d.values():
    print (value)