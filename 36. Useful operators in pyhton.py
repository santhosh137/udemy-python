"""
"""

mylist=[1,2,3]

for i in range(10):
    print (i)

print ("\n")

for i in range(3,10):
    print (i)

print ("\n")

for i in range(0,10,2):
    print (i)

print (list(range(0,11,2)))

index_count=0

for l in 'abcde':
    print ('At index {} the letter is {}'.format (index_count,l))

index_count=0
word='abcde'
for l in word:
    print(word[index_count])
    index_count+=1

## enumerate index count in form of tuples

index_count=0
word='abcde'
for l in enumerate(word):
    print(l)

index_count=0
word='abcde'
for l,l1 in enumerate(word):
    print(l)
    print (l1)
    print ("\n")

mylist1=[1,2,3,4,5]
mylist2=['a','b','c']

for item in zip(mylist1,mylist2):
    print (item)


mylist1=[1,2,3,4,5]
mylist2=['a','b','c']
mylist3=[100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print (item)

print (list(zip(mylist1,mylist2,mylist3)))

print ('x' in [1,2,3])

print ( 'k1' in {'k1':123, 'k2': 'abc'})

d={'k1':123, 'k2': 'abc'}

print (123 in d.keys())

print (d.items())

mylist4=[10,20,30,40]
print(min(mylist4))
print(max(mylist4))

from random import shuffle

mylist5=[1,2,3,4,5,6,7,8,9,10]

shuffle(mylist5)

print (mylist5)

from random import  randint

print (randint(0,90))

mynum=randint(0,90)

result=input("what is your name")

print (result)