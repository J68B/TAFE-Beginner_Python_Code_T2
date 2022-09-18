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


# create a list and variables to store user inputs
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # list will contain all uppercase alphabet characters only
userInput = input("Prepared Text: ")
# create shift variable so that it is modulus and only takes intergers
shift = ''
while shift == '' :
    try:
        shift = int(input("Shift Value: ")) % 26 
    except ValueError:
        print("Please only use whole number values")
        
# create the encrypt_Caesar function,
# This function creates a list from the prepared text, makes changes to each letter based on the shift value, and joins the list as a sting output
def encrypt_Caesar():
    shiftedAlpha = alphaList[shift:] + alphaList[:shift] #create a variable for the shift command
    cipherList = [] # create an empty list for cipherList variable
    for words in userInput: 
        prepText = "" # set placeholder
        for letter in words: 
            prepText += shiftedAlpha[alphaList.index(letter)] # traverses all the letters and updates the prepText variable with the encrypted letter
        cipherList.append(prepText) #appends the cipherList with the letter changes
    global encryptedText
    encryptedText = ("".join(cipherList)) # combines all the encrypted letters and assigns it to a variable, ensuring the letters are joined
    return encryptedText 
    
encryptedText=encrypt_Caesar()
print(encryptedText)

''' PLEASE NOTE: Step 4 tests are included on a seperate .py file called task2tests.py that was uploaded alongside this file'''