def encrypt_char(char, k):
    return chr(ord('A') + (ord(char) - ord('A') + k) % 26)


def em():
    m=input("input message: ")
    k=input("enter shift value: ") 
    cipher = ''
    for char in m:
        if char not in ' ,.':
            cipher += encrypt_char(char, k)
        else:
            cipher += char
    return cipher

em()




    