'''
Author:     Jason Brown
Student ID: 469730808
Date:       20/08/22

There are mulitple codes in this file;
 - one if for Q4 which is commented out as I needed to check the code worked
 - one is for Q7 which includes coding for the tests
 
'''

# Q4 Code
# age=int(input("Enter Age: "))
# if age >= 18:
#     print("You can enter the nightclub")
# else:
#     print("You are too young to enter the nightclub")

# Q7 code
#define the onlydigits function and set 1 parameter
def onlydigits(parameter):
    # join characters and omit anything that is not a number
    result="".join(char for char in argument if char.isdigit())
    
    # return the function
    return result


# Test 1
argument=("Th15 is h0W W3 do%%%% it in 2022")
output=onlydigits(argument)
if (output == "15032022"):
    print("Test 1 OK")
else:
    print("Test 1 error: " + output)
  
# Test 2
argument=("100 divided BY 100 is 1")
output=onlydigits(argument)
if (output =="1001001"):
    print("Test 2 OK")
else:
    print("Test 2 error: " + output)
  
# Test 3
argument=("This is meant to generate an error for test 3")
output=onlydigits(argument)
if (output =="33"):
    print("Test 3 OK")
else:
    print("Test 3 Error: " + "output should be:",output)  