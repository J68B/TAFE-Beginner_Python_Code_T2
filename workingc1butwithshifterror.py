'''
Author:     Jason Brown
Student ID: 469730808
Date:       20/08/22
'''

''' This program will use functions created in task 1 and task 2 with some minor tweaks '''
# load import modules
import sys

# create a list and variables to store user inputs
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # list will contain all uppercase alphabet characters only

# define argument variables
shift="" # placeholder
text=sys.argv[2]

while shift == "" :
    try:
        shift = int(sys.argv[1]) % 26
    except ValueError: 
        shift = ""
        print("ERROR 01 - Please only use whole number values for argument 1 (shift value) ")
        break

    
# shift=int(sys.argv[1]) % 26

def encrypt_Caesar(shift, text):
    rep=text.replace(".", "X")
    repJoin="".join(char for char in rep if char.isalpha())
    output=(repJoin.upper())
    print(output)
    
    shiftedAlpha = alphaList[shift:] + alphaList[:shift] 
    cipherList = [] 
    for words in output: 
        prepText = "" 
        for letter in words: 
            prepText += shiftedAlpha[alphaList.index(letter)] 
        cipherList.append(prepText) 
    global encryptedText
    encryptedText = ("".join(cipherList)) 
    return encryptedText 
    

encryptedText=encrypt_Caesar(shift, text)
print(encryptedText)


# create shift variable so that it is modulus and only takes intergers
