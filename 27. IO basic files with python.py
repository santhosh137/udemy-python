"""
"""


import os
print (os.getcwd())
os.chdir(r"C:\Users\infra\Desktop\sk")

print (os.getcwd())

myfile=open("cred.txt")

print (myfile)

myfile=open("cred.txt",'r')

print(myfile.read())

print(myfile.read())

print (myfile.seek(0))

contents =myfile.read()
#print (contents)

myfile=open("cred.txt",'r')

print (myfile.readlines())


"""----------------------------------------------------------------------"""


"open a text file saved in another location"

myfile=open("C:\\Users\\infra\\Downloads\\missing applications from the given list.txt")

print (os.getcwd())

print(myfile.read())

myfile.close()

with open('cred.txt') as my_new_file:
    contents=my_new_file.read()

print (contents)

"""Reading and writing and overwriting files"""

with open('cred.txt', mode='r') as myfile:
    contents = myfile.read()

# with open('cred.txt', mode='w') as myfile:
#     contents = myfile.read()
#

"""Reading , writing, appending modes
mode='r' is read only
mode='w' is write only 
mode='a' is append only
mode='r+' is reading and writing
mode='w+' is writing  and reading

"""

with open ('my_file_tt.txt',mode='w') as f:
    f.write("Hello, Welcome to the world")

with open ('my_file_tt.txt',mode='r') as f:
    print (f.read())

with open('my_file_tt.txt',mode='a') as f:
    f.write('FOUR ON FOURTH')

fi=open('my_file_tt.txt','r')
print(fi)
print(fi.read)
print(fi.read())
fi.close()