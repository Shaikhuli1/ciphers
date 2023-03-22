import random
import string

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)
 
    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)
 
    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]
 
    return matrix

def encrypt():
    pass

def decrypt():
    pass

if __name__ == "__main__":
    text = input('Enter your text: ')
    choice = input('Please press E for encryption, or D for decryption: ')

    if choice == 'E':
        encrypt()#
    elif choice == 'D':
        decrypt()