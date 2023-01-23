# Master script of all the ciphers will be going here, including encryption and decryption

### Simple Substitution ###
import random
import string

while True:
    choice = input('Please enter (1) for encryption, or (2) for decryption: ')

    if choice == '1':
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
        break
    elif choice == '2':

# Decryption

        dtext = input('Enter the text you want decrypted here: ')
        dkey = input('Enter your encryption key: ')
        alphabet = string.ascii_lowercase
        plaintext = ''
        for letter in dtext:
            if letter.lower() in dkey:
                plaintext += alphabet[dkey.find(letter.lower())]
            else:
                plaintext += letter
        break
        print(f'Your decrypted text: {plaintext}')
        continue

### Caesar Cipher ###
import random

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
