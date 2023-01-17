import random
import string

alphabet = string.ascii_lowercase
key = ''.join(random.sample(alphabet,len(alphabet)))
plaintext = input('Enter the text you want encrypted: ')

ciphertext = ''
for letter in plaintext:
    if letter.lower() in alphabet:
        ciphertext += key[alphabet.find(letter.lower())]
    else:
        ciphertext += letter

print(ciphertext)



