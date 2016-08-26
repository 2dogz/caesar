from sys import argv, exit
from helpers import alpha_position, rotate_character
def user_input_is_valid(cl_args):

    if len(cl_args) < 2:
        print("please enter argument")
        return False
    if cl_args[1].isdigit():
        return True
    else:
        return False

def encrypt(text, rot):
#look at each char in text
    resultstring =""
    for i in text:
        is_upper = False
        is_lower = False
        if i.isupper():
            is_upper = True
        if i.islower():
            is_lower = True
        translated = rotate_character(i, int(rot))
        if is_upper == True:
                resultstring = resultstring + translated.upper()
        elif is_lower == True:
                resultstring = resultstring + translated.lower()
        else:
            resultstring = resultstring + translated
    return(resultstring)
#if user_input_is_valid(argv) == False:
#    exit()
#print(encrypt(text, argv[1]))
