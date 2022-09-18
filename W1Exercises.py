''' Week 1 exercises
Jason Brown
469730808
15/07/22
'''
#-----------------------------------------------------------------------------
'''
# Exercise 1

# Get 3 numbers from user
var1 = int(input("Input first number: "))
var2 = int(input("Input second number: "))
var3 = int(input("Input third number: "))

# Compare the numbers against each other and print the highest number
if var1 > var2 and var1 > var3:
    print("The highest number is the 1st input, which was", var1)
elif var2 > var3 and var2 > var1:
    print("The highest number is the 2nd input, which was", var2)
else:
    print("The highest number is the 3rd input, which was", var3)
'''    

# ------------------------------------------------------------------
'''
# Exercise 3

# Write a Python script to read in a line of text from the user. Examine the text that the user entered,
# and print out a summary of the text:
# • the number of space characters in the text
# • the number of decimal digits in the text (i.e. 0 to 9)
# • the number of vowels in the text (i.e. A, E, I, O, U, a, e, i, o and u)
# • (challenging) the number of consonants (letters that are not vowels) in the text


# set all the variables we want to calculate
spaces=0
numbers=0
vowels=0
consonants=0

# get user input and store it as a variable
sentence=input("Please enter a line of text: ").lower()

# identify what each digit in the sentence is
for letter in sentence:
    if letter == " ":
        spaces = spaces + 1
    if letter.isdigit():
        numbers = numbers + 1
    if letter in ("a","e","i","o","u"):
        vowels = vowels + 1
    if letter in ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"):
        consonants = consonants + 1

# print out the results
print("There are",spaces,"spaces in this sentence")
print("There are",numbers,"numbers in this sentence")
print("There are",vowels,"vowels in this sentence")
print("There are",consonants,"consonants in this sentence")
'''
#-----------------------------------------------------------------------------------------
'''
# Exercise 5

# Here is a set of integer values in a Python list:
#   numList = [ 17, 12, 56, 94, 3, 18, 45, 62, 9, 101, 86, 7 ]
#   print(numList)
# Write a Python script that starts with this list of values.
# Convert the Bubble Sort algorithm into Python,
# so that it sorts the numList into ascending order (smallest to biggest).
# Print out the numList before the sorting. Print out the numList after the sorting.

# Write a Python script that starts with this list of values.
numList = [17,12,56,94,3,18,45,62,9,101,86,7]

# Print out the numList before the sorting.
print("These are the numbers that need to be sorted in ascending order",numList)

# define the bubblesort algorithm for numList
def bubbleSort(numList):
    for num in range(len(numList)-1,0,-1):
        for i in range(num):
            if numList[i]>numList[i+1]:
                temp = numList[i]
                numList[i] = numList[i+1]
                numList[i+1] = temp

# Sort and print the numList into ascending order
bubbleSort(numList)
print()
print("This is the number list sorted in ascending order", numList)

# I installed bubble-sorter from PyPI, although I did not need to import it into the code
# I also used w3resource for the def, as I am still very confused on exactly what is happpening here code wise
# I tested the code using different number values
'''
