# importing the module
import sys

# function definition
def convert_to_Caesar(text):
    rep=text.replace(".", "X")
    print(rep)
    repJoin="".join(char for char in rep if char.isalpha())
    output=(repJoin.upper())
    print(output)
  
# fetching the arguments
text = sys.argv[1]
convert_to_Caesar(text)

