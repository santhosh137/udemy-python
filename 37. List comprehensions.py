"""
list comprehensions are unique way of quickly creating a list with python

if you find yourself using a for loop along with .append() to create a list ,
 list comprehesnions are a good alternative

"""

mystring="hello"

mylist=[]

for l in mystring:
    mylist.append(l)

print (mylist)

mylist1=[i for i in mystring]

print (mylist1)

mylist2=[num for num in range(0,11)]
print (mylist2)

mylist3=[num**num for num in range(0,11)]
print (mylist3)


mylist4=[num**2 for num in range(0,11) if num%2==0]
print (mylist4)

celsius=[0,10,20,34.5]

fahrenheit=[((9/5)*temp +32) for temp in celsius]
print (fahrenheit)


result=[x if x%2==0 else 'ODD' for x in range(0,11)]

print (result)

mylist5=[x*y for x in [2,4,6] for y in [1,10,1000]]

print(mylist5)