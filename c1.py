'''
Author:     Jason Brown
Student ID: 469730808
Date:       11/09/22
'''

''' This program will combine functions created in task 1 and task 2 to produce caesar cipher code in one command line interface '''
# load import modules
import sys
sys.tracebacklimit=0

# create a list and variables to store user inputs
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # list will contain all uppercase alphabet characters only

# define argument variables
shift="" # placeholder for user error checking
text=sys.argv[2]

# checks for user input errors on the command line
while shift == "" :
    try:
        shift = int(sys.argv[1]) % 26
    except (ValueError, TypeError):
        print("ERROR 01 - Please only use whole number values for argument 1 (shift value) ")
        break

# combined functions to produce encrypted text from converted text
def encrypt_Caesar(shift, text):
    rep=text.replace(".", "X")
    repJoin="".join(char for char in rep if char.isalpha())
    output=(repJoin.upper())
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
print("Encrypted text is: ", encryptedText, end="")