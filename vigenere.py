# Vigenere Cipher
import string
alphabet = string.ascii_lowercase


def generate_key(ptext,key):
    keylist = list(key)
    while len(keylist) < len(ptext):
        for i in range(len(ptext) - len(keylist)):
            keylist.append(keylist[i])
    return ''.join(key)

def vign_encr(): 
    pass

    


def vign_decr():
    ctext = input('Enter your text: ')
    shift = input('Enter the shift you want to use: ')

choice = input('Please press E for encryption, or D for decryption: ')

if choice.upper() == 'E':
    ptext = input('Enter your text: ')
    keyword = input('Enter the keyword you want to use: ')
    key = generate_key(ptext,keyword)
    vign_encr()
elif choice.upper() == 'D':
    vign_decr()