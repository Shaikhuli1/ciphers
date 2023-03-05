# Caesar Cipher
import random
'''
def caesar_encr():
    self.string = input('Enter your text: ')
    shift = input('Enter the shift you want to use. Enter "RANDOM" if you wish to generate a random one: ')
    if shift == 'RANDOM':
        shift = random.randint(1,25)

    ctext = ''
    for char in self.string:
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
    self.string = ''
    for char in ctext:
        if char.isupper():
            self.string += chr((ord(char) - shift - 65)% 26 + 65)
        elif char.islower():
            self.string += chr((ord(char) - shift - 97)% 26 + 97)
        else:
            self.string += char

    print(f'Encrypted text: \n{self.string}')

if __name__ == '__main__':
    choice = input('Please press E for encryption, or D for decryption: ')

    if choice.upper() == 'E':
        caesar_encr()
    elif choice.upper() == 'D':
        caesar_decr()
'''
class Shift:
    def __init__(self):
        self.shift = input('Enter the shift you want to use. If encrypting, enter "RANDOM" if you wish to generate a random shift: ')

    def rand_shift(self):
        if self.shift.isdigit():
            return int(self.shift)
        elif self.shift == 'RANDOM':
            self.shift = random.randint(1,25)
            return self.shift

class Cipher:
    def __init__(self):
        self.text = input('Enter your text: ')
        self.shift = Shift().rand_shift()
        self.string = ''
    
    def caesar_encr(self):
        for char in self.text:
            if char.isupper():
                self.string += chr((ord(char) + self.shift - 65)% 26 + 65)
            elif char.islower():
                self.string += chr((ord(char) + self.shift - 97)% 26 + 97)
            else:
                self.string += char

        print(f'Your shift key is: {str(self.shift)}. Keep it safe.')
        print(f'\nEncrypted text: {str(self.string)}')

    def caesar_decr(self):
        for char in self.text:
            if char.isupper():
                self.string += chr((ord(char) - self.shift - 65)% 26 + 65)
            elif char.islower():
                self.string += chr((ord(char) - self.shift - 97)% 26 + 97)
            else:
                self.string += char

        print(f'Decrypted text: \n{str(self.string)}')

class Caesar:
    def __init__(self):
        self.choice = input('Please press E for encryption, or D for decryption: ')
        self.cipher = Cipher()

    def user_choice(self):
        if self.choice.upper() == 'E':
            self.cipher.caesar_encr()
        elif self.choice.upper() == 'D':
            self.cipher.caesar_decr()

if __name__ == '__main__':
    caesar = Caesar()
    caesar.user_choice()