"Find out a word 'dog' is in a function"
#
# def check_dog(my_string):
#     if 'dog' in my_string:
#         print(True)
#     else:
#         return False
#
# check_dog("My dog run away")
#
# check_dog("My Cat run away")
#
# def check_dog(my_string):
#     if 'dog' in my_string.lower():
#         return True
#     else:
#         return False
#
# check_dog("My dog run away")
#
# check_dog("My Cat run away")

def check_dog(my_string):
    print('dog' in my_string.lower())

check_dog("My dog run away")

check_dog("My Cat run away")

"""

PIG LATIN

If a word starts with a vowel, add 'ay' to end

If word does not starts with a vowel, put first  letter at the end, then add 'ay'

"""

def pig_latin(word):
    first_letter=word[0]
    if first_letter in 'aeiou':
        pig_word=word+'ay'
    else:
        pig_word=word[1:]+first_letter+'ay'

    print (pig_word)
    return (pig_word)

pig_latin('word')
pig_latin('apple')