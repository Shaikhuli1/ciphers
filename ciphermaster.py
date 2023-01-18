# Master script of all the ciphers will be going here, including encryption and decryption

# Simple Substitution #
import random
import string

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

dtext = input('Enter the text you want decrypted here: ')
dkey = input('Enter your encryption key: ')