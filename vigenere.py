# Vigenere Cipher
import string
alphabet = string.ascii_lowercase


def generate_key(text,key):
    keylist = list(key)
    while len(keylist) < len(text):
        for i in range(len(text) - len(keylist)):
            keylist.append(keylist[i])
    return ''.join(key)

def vign_encr(ptext,key): 
    ctext = ''
    for i in range(len(ptext)):
        x = (ord(ptext[i]) + ord(key[i])) % 26
        x += ord('A')
        ctext += chr(x)
    return ctext
    
def vign_decr(ctext,key):
    ptext = ''
    for i in range(len(ctext)):
        x = (ord(ctext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        ptext += chr(x)
    return ptext

choice = input('Please press E for encryption, or D for decryption: ')

if choice.upper() == 'E':
    ptext = input('Enter your text: ')
    keyword = input('Enter the keyword you want to use: ')
    key = generate_key(ptext,keyword)
    ctext = vign_encr(ptext,key)
    print(f'Cipher text: {ctext}')
elif choice.upper() == 'D':
    ctext = input('Enter your text: ')
    keyword = input('Enter the keyword you want to use: ')
    key = generate_key(ctext,keyword)
    ptext = vign_decr(ctext,key)
    print(f'Decrypted text: {ptext}')