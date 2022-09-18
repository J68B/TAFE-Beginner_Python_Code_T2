# Define the function
def convert_to_Caesar(variable):

    # Allow python to access Regular Expression
    import re
    
    # Allow the script to cite plainText outside of the function
    global plainText
    
    # Give the input a variable
    
    plainText = (str(variable)
    # plainText = (str("What would you like to encrypt? ")
                 
    .upper() # Convert input to capital letters
    .replace(" ", "") # Removes spaces in the sentence
    .replace(".", "X") # Replaces periods with the letter 'X'
    )
    
    # Discards all characters other than A-Z (Makes any input outside of A-Z invalid)
    resub = re.sub(r'[^A-Z]+', '', plainText)

    # Joins the resub string to the final output
    plainText = resub
    
    # Output the variable
    return plainText


def encrypt_Caesar(x):
    shift = 3 # defining the shift count
    
    text = plainText
    
    global encryption
    
    encryption = ""
    
    for c in text:

        # find the position in 0-25
        c_index = ord(c) - ord("A")

        # perform the shift
        new_index = (c_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    return encryption





def call(x):
    convert_to_Caesar(x)
    encrypt_Caesar(x)
    

# Test 1
result = encrypt_Caesar('Hello there')
print(result)