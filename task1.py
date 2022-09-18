'''
Author:     Jason Brown
Student ID: 469730808
Date:       25/07/22
'''

# the keyboard input is commented out for testing purposes only
# userInput=input("What did you want to say: ")

# setting a place holder variable for output, which is going to become a global variable
output=("")

# define a function to prepare a string of text for caeser cypher conversion
def convert_to_Caesar():
    # replace and period/fullstops with a capital X
    rep=userInput.replace(".", "X")
    # join characters and omit anything that is not in the alphabet
    repJoin="".join(char for char in rep if char.isalpha()) # this command also removes spaces
    # make the output variable global for testing purposes
    global output
    #convert lower case character to uppercase and display the result
    output=(repJoin.upper())
       

# define a compare function for testing the output after it has been converted to caesar
def compare():
    if expected == output:
        print("--> TEST OK")
    else:
        print("--> TEST FAILED: ")
        print("--> Expected should have been,", output, "however it was: ", expected)
        print("--> Check the two manual entries: 'userInput' and 'Expected' for typos.")
        print("--> If manual entries are correct, check algorithm and convert_to_Caesar function code.")

# define a newline function to save time formating the look at the end of each test, so changes can be made easily
def newline():
    print()
    print("*************************************************************************************************************")
    print()   
        

# Test 1
print("Test 1 Conversion") # I wanted to not just test the code but also visually see what is occuring
userInput=("whats doin mate")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected") # this will test converted output vs expected output
expected=("WHATSDOINMATE")
print("Expected text is: ", expected)
compare()
newline() # created a funtion to add in some spacing at the end of each test for ease of reading
 
#Test 2
print("Test 2 Conversion")
userInput=("I lost 300 gambling")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("I lost 300 gambling") #purposely making an error in the expected variable for test 2
print("Expected text is: ", expected)
compare()
newline()

#Test 3
print("Test 3 Conversion")
userInput=("You lost $300 gambling???")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("YOULOSTGAMBLING")
print("Expected text is: ", expected)
compare()
newline()

#Test 4
print("Test 4 Conversion")
userInput=("yes I’m so f#ckin ANgRY")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("YESIMSOFCKINANGRY")
print("Expected text is: ", expected)
compare()
newline()

#Test 5
print("Test 5 Conversion")
userInput=("Don’t you DARE tell my wif3*&(!")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("DONTYOUDARETELLMYWIF")
print("Expected text is: ", expected)
compare()
newline()

#Test 6
print("Test 6 Conversion")
userInput=("OK!!, I won’t, if you pay me $300")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("OKIWONTIFYOUPAYME")
print("Expected text is: ", expected)
compare()
newline()

#Test 7
print("Test 7 Conversion")
userInput=("WhatKINDOF friend ru?????  ???")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("WHATKINDOFFRIENDRU")
print("Expected text is: ", expected)
compare()
newline()

#Test 8
print("Test 8 Conversion")
userInput=("The kind, that likes to make sureHiS mate,s learn thIer lessons W3ll, so now you lost SIX HUNDRED DOLLARS gambling!!!")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("THEKINDTHATLIKESTOMAKESUREHISMATESLEARNTHIERLESSONSWLLSONOWYOULOSTSIXHUNDREDDOLLARSGAMBLING")
print("Expected text is: ", expected)
compare()
newline()

#Test 9
print("Test 9 Conversion")
userInput=("Ok, that’s fair, whats your account #")
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print()
print("Now testing conversion vs what is expected")
expected=("OKTHATSFAIRWHATSYOURACCOUNT")
print("Expected text is: ", expected)
compare()
newline()

#Test 10
print("Test 10 Conversion")
userInput=('BSB + "123456”,        Account # - 654321.     don’t gamble again……. XOXO')
print("User input is: ", userInput)
convert_to_Caesar()
print("This converts to: ", output)
print("Now testing conversion vs what is expected")
expected=("BSBACCOUNTXDONTGAMBLEAGAINXXOXO")
print("Expected text is: ", expected)
compare()
newline()

'''Doucmentation of on-paper testing

All tests were performed using the algorithm below, 

Step 1
action: get input sentence

Step 2
action: remove all spaces
reason: this also joins the characters together

Step 3 
action: replace all full stops (“.”) with a capital X (“X”)
reason: ensures the full stop/period is converted to a capital "X" not a lower-case "x" 

Step 4
action: remove all characters that are not alphabet
reason: this will remove everything that is not defined as an alphabet character

Step 5
action: convert all characters to uppercase(capitals)
reason: will convert all lower-case to uppercase and not remove uppercase characters that already exist

Example
action: using test case 6
Step 1 - get the sentence                   | OK!!, I won't, if you pay me $300
Step 2 - remove all spaces                  | OK!!,Iwon't,ifyoupayme$300
Step 3 - replace '.' with 'X'               | OK!!,Iwon't,ifyoupayme$300
Step 4 - remove non alphabet characters     | OKIwontifyoupayme
Step 5 - conver lowercase to uppercase      | OKIWONTIFYOUPAYME

'''






