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

ptext = input('Enter your text: ')
shift = input('Enter the shift you want to use. Enter "RANDOM" if you wish to generate a random one: ')
if shift == 'RANDOM':
    shift = random.randint(1,25)