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
        
    elif choice == '2':

# Decryption

        dtext = input('Enter the text you want decrypted here: ')
        dkey = input('Enter your encryption key: ')
        alphabet = string.ascii_lowercase
    else:
        print('Please enter either 1 or 2.')
        continue

