'''
Author:     Jason Brown
Student ID: 469730808
Date:       10/08/22
Test code will be uploaded as a separate file called task2tests.py
'''

''' The purpose of this function (encrypt_Caesar) is to convert a prepared string of text
(which will contain only uppercase letters) from our previous task1 (convert_to_Caesar) into Caesar code,
based on the user entered shift value.  
for example, if we have the following variables;
- prepared text = "THE"
- shift value = 1
then "THE" would become caesar encoded to "UIF" as;
- T becomes U, when shifted 1 place along the alphabet
- H becomes I, when shifted 1 place along the alphabet 
- E becomes F, when shifted 1 place along the alphabet

*************************************************************************************************************
** IMPORTANT: This function is designed based on task1 function that will prepare an input                 **
** This means that the userInput variable must only contain uppercase letters as per the output in task1   **
** Therefore, this function is not designed to work with numbers, symbols, lower case letters as userInput **
*************************************************************************************************************

'''

import sys

# create a list and variables to store user inputs
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # list will contain all uppercase alphabet characters only
shift=int(sys.argv[1])
userInput=sys.argv[2]

# create the encrypt_Caesar function,
def encrypt_Caesar(shift, userInput):
    shiftedAlpha = alphaList[shift:] + alphaList[:shift] 
    cipherList = [] 
    for words in userInput: 
        prepText = "" 
        for letter in words: 
            prepText += shiftedAlpha[alphaList.index(letter)] 
        cipherList.append(prepText) 
    global encryptedText
    encryptedText = ("".join(cipherList)) 
    return encryptedText 
    
encryptedText=encrypt_Caesar(shift, userInput)
print(encryptedText)