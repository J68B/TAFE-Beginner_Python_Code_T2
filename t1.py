'''
Author:     Jason Brown
Student ID: 469730808
Date:       11/09/22
'''

import sys

# define a function to prepare a string of text for caeser cypher conversion
def convert_to_Caesar(text):
    # replace and period/fullstops with a capital X
    rep=text.replace(".", "X")
     
    # join characters and omit anything that is not in the alphabet
    repJoin="".join(char for char in rep if char.isalpha()) # this command also removes spaces
    
    #convert lower case character to uppercase and display the result
    output=(repJoin.upper())
    print(output)

userInput=sys.argv[2]
convert_to_Caesar(userInput)
