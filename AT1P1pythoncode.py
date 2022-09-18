s=input()
new_str="this is a etst"
for i in range (len(s)):
    if i.isupper():
        new_str+=i.lower()
    elif i.islower():
        new_str+=i.upper()
    else:
        new_str+=i
print(new_str)


# def swap_string():
# 	s=input()
# 	swapped_string=""
# 	swapped_string+=s.swapcase()
#     return swapped_string


# #take input
# string = input('Enter any string: ')
# 
# # upper() function to convert lowercase to uppercase
# print('In Upper Case:', string.upper())


# import string
# 
# def caesar(text, shift, alphabets):
#     
#     def shift_alphabet(alphabet):
#         return alphabet[shift:] + alphabet[:shift]
#     
#     shifted_alphabets = tuple(map(shift_alphabet, alphabets))
#     final_alphabet= ''.join(alphabets)
#     final_shifted_alphabet = ''.join(shifted_alphabets)
#     table = str.maketrans(final_alphabet, final_shifted_alphabet)
#     return text.translate(table)
# 
# plain_text = "This is a new test, hello World!!"
# print(caesar(plain_text, 0, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))














# # Caesar Function
# # 
# # get input from user as a string
# strText=input("Please enter your line of text :")
# # print(strText)
# # calculate the string length (including spaces even after the end of the text)
# print(len(strText))
# # assign variable to string length, VAR = strLen
# stringLength=(len(strText))
# # set a starting variable for string length
# strLen=0
# # WHILE string length is less than or equal to strLen perform the while loop
# WHILE strLen >= stringLength:
#     IF ch.isdigit()
#         print ch
# # IF character in string is UPPERCASE letter
# # 		print character
# # 		strLen = strLen +1
# # 	IF character in string is lower case letter
# # 		convert character to UPPERCASE letter
# # 		print character
# # 		strLen = strLen +1
# # IF character in string is numeric digit 
# # 		strLen = strLen +1
# # 	IF character in sting is a space “”
# # 		strLen = strLen +1
# # 	IF character is a full stop “.”
# # 		print X
# # 		strLen = strLen +1
# # 	ELSE for any other character in string
# # 		strLen = strLen +1
# # 		
# #
