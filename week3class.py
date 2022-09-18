# Week 3 Class

'''
# def sameString(firstString, secondString):
#     if firstString == secondString:
#         return True
    
# 
# firstString = input("Give me a string: ")
# 
secondString = input("Give me another string: ")

# if (sameString (firstString, secondString)):
#     print("They are the same")
# else:
#     print("They are different")
'''
import sys

def compare(a,b):
    if a.lower() == b.lower():
        return(True)
    

a=sys.argv[1]
b=sys.argv[2]
# input("First string: ")
# b=input("Second string: ")
if compare(a,b):
    print("They are the same")
else:
    print("They are not the same")





# def cuppa(sentence):
#     count = 0
#     for char in sentence:
#         if char >= 'A' and char <= 'Z':
#             count = count +1
#     return(count)
#         
# sentence=input("Enter a line of text: ")
# count=cuppa(sentence)
# print("That has", count, "uppercase letters")






#a and b are the argument variables
# if a is bigger, return that
# otherwise return b
# 
# def maxOfValues(a,b,c):
#     if a > b and a > c:
#         return(a)
#         
#     elif b > a and b > c:
#         return(b)
#     
#     else:
#         return(c)
# 
# x=input("first number: ")
# y=input("second number: ")
# z=input("third number: ")
# max=maxOfValues(x,y,z)
# print("The max is", max)