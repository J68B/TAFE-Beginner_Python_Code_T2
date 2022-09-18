'''
Author:     Jason Brown
Student ID: 469730808
Date:       20/08/22
'''

''' This program will use functions created in task 1 and task 2 with some minor tweaks '''

import sys

# setting a place holder variable for output, which is going to become a global variable
# output=("")


# function that prepares the users input text for caeser cypher conversion
def convert_to_Caesar(a1):
    rep=arg1.replace(".", "X") # replace and period/fullstops with a capital X
    repJoin="".join(char for char in rep if char.isalpha()) # join characters and omit anything that is not in the alphabet, also removes spaces
    global output # make the output variable global
    output=(repJoin.upper()) #convert lower case character to uppercase and display the result
    return


cts=convert_to_Caesar(arg1)
print(cts)




# # create a list and variables to store user inputs
# alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # list will contain all uppercase alphabet characters only
# userInput = output 
# shift = '' 
# 
# # create shift variable so that it is modulus and only takes intergers
# while shift == '' : 
#     try:
#         shift = int(input("Shift Value: ")) % 26 
#     except ValueError:
#         print("ERROR 01 - Please only use whole number values")
# 
# # create the encrypt_Caesar function
# def encrypt_Caesar(shift):
#     shiftedAlpha = alphaList[shift:] + alphaList[:shift]
#     cipherList = []
#     for words in userInput:
#         prepText = ""
#         for letter in words:
#             prepText += shiftedAlpha[alphaList.index(letter)]
#         cipherList.append(prepText)
#     global encryptedText
#     encryptedText = ("".join(cipherList))
#     return encryptedText
#     
# encrypt_Caesar(3)
# print("Coded message: ",encryptedText)

