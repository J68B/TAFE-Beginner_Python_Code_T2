'''
Author:     Jason Brown
Student ID: 469730808
Date:       11/09/22
'''

''' This program will combine functions created in task 1 and task 2 to produce caesar cipher code in one command line interface '''

# load import modules
import sys

# create a list of uppercase letters
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 

# define a function to produce encrypted text from converted text
def encrypt_Caesar(shift,text):
    # convert full stops to upper case X, remove numbers, spaces, symbols, and convery lower case letters to uppercase 
    rep=text.replace(".", "X")
    repJoin="".join(char for char in rep if char.isalpha())
    output=(repJoin.upper())
    
    # encrypt converted user text using predefined alpha list and user shift value
    shiftedAlpha = alphaList[shift:] + alphaList[:shift] 
    cipherList = [] 
    for words in output: 
        prepText = "" 
        for letter in words: 
            prepText += shiftedAlpha[alphaList.index(letter)] 
        cipherList.append(prepText) 
    encryptedText = ("".join(cipherList)) 
    return encryptedText 
        

# for generating error codes based on different types of user error
while True:
    # ensure user input has 3 arguments
    if len(sys.argv) != 3:
        print("Error 00: Parameter Error - requires 3 arguments: program name(caesar.py), shift value(user defined whole number), and user text(user defined in double quotes)")
        break
    
    # assign argument variables for shift value and user text
    else:
        shiftVal=sys.argv[1]
        userText=sys.argv[2]
        
        try:
            shiftVal = int(shiftVal)
        # generate an error if 3 parameters are not used
        except ValueError:
            print("Error 01: Value Error - Please only use whole numbers (integers) for shift value")
            break
        # generate an error if shift value is not in range
        if shiftVal <= -26 or shiftVal >= 26:
            print("Error 02: Range Error - Please enter a positive or negative whole number between 1 and 25 inclusive")
            break
        
        # perform conversion and encryption if no errors
        else:
            encryptedUserText=encrypt_Caesar(shiftVal,userText)
            print("Encrypted text is: ", encryptedUserText)
            break