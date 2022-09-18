# ## Show the contents of a file
# 
# fileName = input("Name of text file: ")

# # Open the file
# inputFile = open(fileName, "r")
# 

# Loop to read and print
# 
# for line in inputFile:
#     print(line, end="")
    
#     
# # close the file
# inputFile.close()


## WRITE TO A FILE
# create the file
#     fileName = input("Name of text file to create: ")

# 
# # open the file
# 
# outputFile = open(fileName, "w")
# 
# 

# Write some stuff
# outputFile.write("Wassup!!")
# outputFile.write("Each line must be a string:" + str(23))
# outputFile.write("One last line for the file")
# 
# # close the file
# 
# outputFile.close()
sentence = "one fine day in Paris"
position = sentence.find("day")
print("Position is", position)
print(sentence.capitalize())



