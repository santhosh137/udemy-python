"""

Control flow

certain code to execute , when aparticular condition has been met.

For example, if my dog is hungry , then i will feed my dog


keywords

if
elif
else

Control flow syntax that makes use of colons and indentations

The indentation system is crucial to python and is wjat sets it apart from other
pprogramming languages


if condition:
 statement 1
else:
 statement 2


if condition 1:
 statement 1
elif condition 2:
 statement 2
else:
 statement 3

"""

if True:
    print ("1")
else:
    print ("2")


if 3>2:
    print ("1")
else:
    print ("2")

hungry=True

if hungry:
    print ("FEED ME")
else:
    print ("NOT FEED ME")


loc='Bank'

if loc=='Auto shop':
    print ('cars are cool')
elif loc=='Bank':
    print("Money is cool")
else:
    print ('I dont know much')

name='Sam'

if name=="Frank":
    print ("Hello Frank")
elif name=="Sammy":
    print ("Hello Sammy")
else:
    print ("What is your name")