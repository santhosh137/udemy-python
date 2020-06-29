"""
Creating a clean repeatable code is a key part of becoming abn effective programmer

Functions allow us to create blocks of code that can be easily executed many times, without needing to constantly
  rewrite the tntire block of code

def Func_name():
    "Docstring"
    print ("Hello")

Func_name()

def Func_name(name):
    "Docstring"
    print ("Hello" + name)

Func_name(name)

Typically we use the  return keyword to send back the result of the fucntion, instead of
just printing it out.

return allows us to assign the output of the fucntion to a new variable

def add_func(num1, num2):
    return (num1+num2)

Result=add_func(2,3)

"""

def Customer():
    print ("HELLO")

Customer()

def name_function():
    '''
    DOCSTRINHG
    INPUT : HELLO
    Ouptut : Hello Name
    '''
    print ("Hello")

def Customer(name):
    print ("HELLO", name)

Customer("Santhosh")

def Customer(name="SANTHOSH"):
    print ("HELLO", name)

Customer()

def Customer(name="SANTHOSH"):
    return ("HELLO", name)

Customer("David")

Result=Customer("ZAch")
print (Result)


def Customer(name="SANTHOSH"):
    return ("HELLO "+ name)

Customer("David")

Result=Customer("ZAch")
print (Result)



def Customer(name):
    print ("HELLO", name)

Customer("Good day to you")

def add(n1,n2):
    return n1+n2

print (add(3,2))


