some_value="100"

print (some_value.isdigit())

def user_choice():
    choice="WRONG"
    while choice.isdigit()==False:
        choice=input("Please enter a number(0-10): ")

        if choice.isdigit() == False:
            print ("Sorry that is not a digit")

    print (int(choice))


user_choice()

result="WRONG"

accetable_values =[0,21,2,4]

print (result in accetable_values)

print (result  not in accetable_values)

def user_choice1():
    choice="WRONG"
    acceptable_range=range(10)
    within_range=False


    while choice.isdigit()==False or within_range==False:
        choice=input("Please enter a number(0-10): ")

        if choice.isdigit() == False:
            print ("Sorry that is not a digit11")

        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                within_range=False

    print (int(choice))

user_choice1()