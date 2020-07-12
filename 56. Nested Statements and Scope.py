x=25

def printer():
    x=50

    print(x)

print (x)

print (printer())

"""
LEGB RULE

L- local - names assigned in a way within a function (def or lambda),
and not declared global in that function

E- Enclosing function locals - Names in the local scope of any and all enclosing functions
from inner to outer

G- Global - Names assigned at the  top level of a module file or declated global in a def within  the file.

B- Built in - Names preassigned in the built in names moduel
open, range, syntaxerror, os

"""


# lambda num : num**2

name="THis is a glkobal string"

def greet():
    #name="Sammy"

    def hello():
        print ("Hello "+ name)

    hello()
greet()