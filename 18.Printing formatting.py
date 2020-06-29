"""

injecting a variable to string

my_name= "Jose"
print ("hello" + my_name)

There are multiple ways tyo format string for printing the variables in them

This is known as string interpolation

Two methdos for this

.format()

f-strings


"""

print ("This is a string {}".format ('INSERTED'))

print ("The {} {} {}  ".format('fox', 'brown','quick'))

print ("The {2} {1} {0}  ".format('fox', 'brown','quick'))

print ("The {0} {0} {0}  ".format('fox', 'brown','qui0ck'))

print ('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

'Float formatiing follows "{value:width.precision f}"'

result = 100/777
print (result)

print ("The result was {}".format (result))

print ("The result was {r}".format (r=result))

print ("The result was {r: 1.4}".format (r= result))

print ("The result was {r: 1.4f}".format (r= result))

name="Jose"
age=3

print ("Hello, his name is {name}")

print (f' {name} is {age} years old')



