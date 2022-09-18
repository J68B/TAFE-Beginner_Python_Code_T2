# My List of Functions


# define a function to prepare a string of text for caeser cypher conversion
def convert_to_Caesar():
    # replace and period/fullstops with a capital X
    new=userInput.replace(".", "X")
    # join characters if they are part of the alphabet
    newJoin="".join(char for char in new if char.isalpha())
    # making the variable global for testing purposes, can use this or not
    global output
    #convert lower case character to uppercase and display the result
    output=(newJoin.upper())
    print(output)


# define a compare function for testing the output after it has been converted to caesar
# can changed variables to suit
def compare():
    if expected == output:
        print("--> TEST OK")
    else:
        print("--> TEST FAILED: ", "Expected should have been,", output, "however it was: ", expected)
        print("Check manual entry, and if that matches review convert_to_caesar function code")


# define a newline code to save time formating the look at the end of each test, so changes can be made easily
def newline():
    print()
    print("*************************************************************************************************************")
    print()


# create the encrypt_Caesar function
def encrypt_Caesar():
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
    
encryptedText=encrypt_Caesar()
print(encryptedText)    