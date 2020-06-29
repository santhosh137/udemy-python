"""
Lists are ordered sequences that can hold a variety of object types
They use [] brackets and commas to separate objects in the list
Lists support indexing and slicing. lists can be nested and also have a variety of
useful methods that can be called off of them



"""

my_list =[1,2,4]

my_list=['STRING', 100,23.3]
print (len(my_list))

my_list =["one", "two", "three", "Four"]

print (my_list[0])

print (my_list[1:])

another_list=["Four", "five"]

new_list=my_list + another_list

print (new_list)

new_list[0]="ONE ALL CAPS"

print (new_list)

new_list.append("six")
print (new_list)

new_list.pop()

print (new_list)

popped_item =new_list.pop()

print (new_list)

popped_item =new_list.pop(0)

print (new_list)
new_list =['a', 'e','i','o','u']

num_list =[4,1,8,3]

new_list.sort()

print (new_list)

my_sort=new_list.sort()

print (my_sort)

new_list.sort()

my_sort=new_list

print (my_sort)

num_list.sort()

sortl=num_list

print(sortl)

num_list.reverse()

print (num_list)