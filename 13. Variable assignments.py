"""
Assingning a vaiable

Rules for choosing a variable name
Name cannot start with a number
Tehre can be no spaces in the name, use _ instead

Cant use any of these special characters

avoid useing words that have special meaning in python like list and str

python uses dynamic typing
This meand you can reassign variables to different data types

This makes python very flexible in assigning data types, this is different than other languages that are
statistically typed

Pros of Dynamic typing
Very easy to work wiht
Faster development time

Cons of Dynamic typing
may result in bug s for unexpected data types
You need to be aware of type ()

"""

my_dogs =2
print (my_dogs)
my_dogs ="Sammy"
print (my_dogs)

a=5
print (a)
a=10
print (a)
a+a
print (a)
a=a+a
print (a)

print (type(a))
a=30.1
print (a)
print (type(a))

my_income =100
tax_rate =0.1
my_tax = my_income * tax_rate
print (my_tax)