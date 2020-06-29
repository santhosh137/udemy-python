"""
While loops will continue to execute a block of code while some condition remains true.

For example, while my pool is not full, keep filling my pool with water

or whil my dogs are still hungry, keep feeding my dogs

while some_boolean_condition:
    do something


while some_boolean_condition:
    do something
else:
    do something different


break
 breaks out ot the current closest enclosing loop

continue
Goes to the top of the closest enclosing loop.

pass
Does nothing at all
"""

x= [1,2,3]

for i in x:
    pass



x=0

while x<5:
    print (x)
    x=x+1
     #x+=1
else:
    print ("x is not less than 5\n")

mystring="Sammy"

for letter in mystring:
    if letter=="a":
        continue
    print (letter)

print ("\n")
for letter in mystring:
    if letter=="a":
        break
    print (letter)

print ("\n")
x=0

while x<5:
    if x==2:
        break
    print (x)
    x=x+1