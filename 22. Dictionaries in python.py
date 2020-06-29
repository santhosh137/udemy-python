"""


Dictiobnaries are unordered mappings for storing objects. previously we saw how lists store onjects n an unordered sequence
dictionaries use a key value pair instead

This key value pair allows users to quickly grab objects without needing to know an
index location

Dictionaries use curly braces and colons  to signify keys and their associated values

{key 1: Value 1, key 2 : Value 2}

So when to choose a list and when to choose a dictionary

Dictionaries : Objects retrieved by key name
Unordered and cannot be sorted.
Lists : Objects retrieved by location
Ordered sequence can be indexed or sliced

"""

my_dict={'key1': 'value1','key2': 'value2','key3': 'value3'}

print (my_dict)

print (my_dict['key1'])

prices_lookup={'apple': 2.99, 'oranges':1.99, 'milk': 5.80, 'apple': 3.50}

print(prices_lookup['apple'])

d={'k1': 123, 'k2':[1,2,3,4,5],'k3': (12,34,'hi'),'k4':{'insidekey':100}}

print (d)

print (d['k4'])
print (d['k4']['insidekey'])

d['k2']="567"

print (d)

d1={'k1':100,'k2':200,'k3':'300'}

d1['k4']='400'

print (d1)

print (d.keys())

print (d.values())

print(d.items())