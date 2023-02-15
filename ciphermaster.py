# Master script of all the ciphers will be going here, including encryption and decryption

### Simple Substitution ###
import random
import string

def ss_encr():
# Encryption
    alphabet = string.ascii_lowercase
    key = ''.join(random.sample(alphabet,len(alphabet)))
    plaintext = input('Enter the text you want encrypted: ')

    ciphertext = ''
    for letter in plaintext:
        if letter.lower() in alphabet:
            ciphertext += key[alphabet.find(letter.lower())]
        else:
            ciphertext += letter

    print(f'Your encryption key is {key}. Please keep it safe!')
    print(f'Your encrypted text: {ciphertext}')
        
# Decryption
def ss_decr():
    dtext = input('Enter the text you want decrypted here: ')
    dkey = input('Enter your key: ')
    alphabet = string.ascii_lowercase
    plaintext = ''
    for letter in dtext:
        if letter.lower() in dkey:
            plaintext += alphabet[dkey.find(letter.lower())]
        else:
            plaintext += letter

    print(f'Your decrypted text: {plaintext}')

choice = input('Please press E for encryption, or D for decryption: ')

if choice.upper() == 'E':
    ss_encr()
elif choice.upper() == 'D':
    ss_decr()

### Caesar Cipher ###

def caesar_encr():
    ptext = input('Enter your text: ')
    shift = input('Enter the shift you want to use. Enter "RANDOM" if you wish to generate a random one: ')
    if shift == 'RANDOM':
        shift = random.randint(1,25)

    ctext = ''
    for char in ptext:
        if char.isupper():
            ctext += chr((ord(char) + shift - 65)% 26 + 65)
        elif char.islower():
            ctext += chr((ord(char) + shift - 97)% 26 + 97)
        else:
            ctext += char

    print(f'Your shift key is: {shift}. Keep it safe')
    print(f'Encrypted text: \n{ctext}')

def caesar_decr():
    ctext = input('Enter your text: ')
    shift = input('Enter the shift you want to use: ')
    ptext = ''
    for char in ctext:
        if char.isupper():
            ptext += chr((ord(char) - shift - 65)% 26 + 65)
        elif char.islower():
            ptext += chr((ord(char) - shift - 97)% 26 + 97)
        else:
            ptext += char

    print(f'Encrypted text: \n{ptext}')

choice = input('Please press E for encryption, or D for decryption: ')

if choice.upper() == 'E':
    caesar_encr()
elif choice.upper() == 'D':
    caesar_decr()

### Vigenere Cipher ###

import string

def generate_key(text,key):
    keylist = list(key)
    while len(keylist) < len(text):
        for i in range(len(text) - len(keylist)):
            keylist.append(keylist[i])
    return ''.join(keylist)

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
text = input('Enter your text: ').upper().replace(' ','')
keyword = input('Enter the keyword you want to use: ').upper()


if choice.upper() == 'E':
    key = generate_key(text,keyword)
    ctext = vign_encr(text,key)
    print(f'Cipher text: {ctext}')
elif choice.upper() == 'D':
    key = generate_key(text,keyword)
    ptext = vign_decr(text,key)
    print(f'Decrypted text: {ptext}')