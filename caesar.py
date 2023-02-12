# Caesar Cipher
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

if __name__ == '__main__':
    choice = input('Please press E for encryption, or D for decryption: ')

    if choice.upper() == 'E':
        caesar_encr()
    elif choice.upper() == 'D':
        caesar_decr()
