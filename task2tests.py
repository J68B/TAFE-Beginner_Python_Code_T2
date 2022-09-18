'''
Author:     Jason Brown
Student ID: 469730808
Date:       10/08/22
'''

''' This is a set of 11 tests to determine if our encrypt_Caesar function is working as intended '''

# create required variables for the tests
alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
shift = ''
      
# encrypt_Caesar function
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

# utilising previously created functions from task1, newline() and compare()
def newline():
    print()
    print("*************************************************************************************************************")
    print()   

def compare():
    if expected == encryptedText:
        print("--> TEST OK")
    else:
        print("--> TEST FAILED: ")
        print("--> Expected should have been,", encryptedText, "however it was: ", expected)
        print("--> Check the manual entries: 'userInput', 'shift' and 'expected' for typos.")
        print("--> If manual entries are correct, check algorithm and encrypt_Caesar function code.")


# Test 1
print("Test 1 Encryption")
userInput=("WHATSDOINMATE")
print("User input is: ", userInput)
shift=1 
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") # this will test converted output vs expected output
expected=("XIBUTEPJONBUF")
print("Expected text is: ", expected)
compare()
newline()


# Test 2
print("Test 2 Encryption")
userInput=("XIBUTEPJONBUF")
print("User input is: ", userInput)
shift=-1
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("WHATSDOINMATE")
print("Expected text is: ", expected)
compare()
newline()

# Test 3
print("Test 3 Encryption")
userInput=("ILOSTGAMBLING")
print("User input is: ", userInput)
shift=3
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("LORVWJDPEOLQJ")
print("Expected text is: ", expected)
compare()
newline()

# Test 4
print("Test 4 Encryption")
userInput=("LORVWJDPEOLQJ")
print("User input is: ", userInput)
shift=-3
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("ILOSTGAMBLING")
print("Expected text is: ", expected)
compare()
newline()

# Test 5
print("Test 5 Encryption")
userInput=("YOULOSTGAMBLING")
print("User input is: ", userInput)
shift=13
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("LBHYBFGTNZOYVAT")
print("Expected text is: ", expected)
compare()
newline()

# Test 6
print("Test 6 Encryption")
userInput=("LBHYBFGTNZOYVAT")
print("User input is: ", userInput)
shift=-13
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("YOULOSTGAMBLING")
print("Expected text is: ", expected)
compare()
newline()

# Test 7
print("Test 7 Encryption")
userInput=("YESIMSOFCKINANGRY")
print("User input is: ", userInput)
shift=27 %26
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("ZFTJNTPGDLJOBOHSZ")
print("Expected text is: ", expected)
compare()
newline()

# Test 8
print("Test 8 Encryption")
userInput=("ZFTJNTPGDLJOBOHSZ")
print("User input is: ", userInput)
shift=-27 % 26
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected") 
expected=("YESIMSOFCKINANGRY")
print("Expected text is: ", expected)
compare()
newline()

# Test 9
print("Test 9 Encryption")
userInput=("THEKINDTHATLIKESTOMAKESUREHISMATESLEARNTHIERLESSONSWLLSONOWYOULOULOSTSIXHUNDREDDOLLARSGAMBLING")
print("User input is: ", userInput)
shift=1234567890 %26
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected")
expected=("DROUSXNDRKDVSUOCDYWKUOCEBORSCWKDOCVOKBXDRSOBVOCCYXCGVVCYXYGIYEVYEVYCDCSHREXNBONNYVVKBCQKWLVSXQ")
print("Expected text is: ", expected)
compare()
newline()

# Test 10
print("Test 10 Encryption")
userInput=("DROUSXNDRKDVSUOCDYWKUOCEBORSCWKDOCVOKBXDRSOBVOCCYXCGVVCYXYGIYEVYEVYCDCSHREXNBONNYVVKBCQKWLVSXQ")
print("User input is: ", userInput)
shift=-1234567890 %26
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected")
expected=("THEKINDTHATLIKESTOMAKESUREHISMATESLEARNTHIERLESSONSWLLSONOWYOULOULOSTSIXHUNDREDDOLLARSGAMBLING") 
print("Expected text is: ", expected)
compare()
newline()

# Test 11 # adding a test without modulus included in the shift variable to induce an error
print("Test 11 Encryption")
userInput=("OKTHATSFAIRWHATSYOURACCOUNT")
print("User input is: ", userInput)
shift=27 
print("Shift value is: ", shift)
encrypt_Caesar()
print("This converts to: ", encryptedText)
print()
print("Now testing conversion vs what is expected")
expected=("PLUIBUTGBJSXIBUTZPVSBDDPVOU")
print("Expected text is: ", expected)
compare()
newline()




# Next step is to create a file using the date and time and give an option to output the result to a file. 
# ##### TEST CODE THAT WILL OUTPUT TO A FILE #####
# 
# # create an output file name
# from datetime import datetime # import the datetime module
# currentDatetime = datetime.now() # call the current date and time and store it as a variable
# currentDateHourMin=currentDatetime.strftime("%d-%m-%y_%H.%M") # create a variable that stores the current date-hr-min
# currentDateHourMin = str(currentDateHourMin) # convert current date-hr-min to a string for concatenation into a filename
# fileName = "task2tests."+currentDateHourMin+".txt" # create a text file
# print("File created: ", fileName) # display the created filename
# newline()
# 
# 
# # create the option
# outputChoice=input("If you would like to output the results to a file, press 1, otherwise press any other key: ")
# if outputChoice==1:
#     import sys 
#     stdoutOrigin=sys.stdout 
#     sys.stdout = open(fileName, "w")
#     sys.stdout.close()
#     sys.stdout=stdoutOrigin

     
