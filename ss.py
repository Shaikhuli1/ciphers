import random
import string
'''
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

if __name__ == '__main__':
    choice = input('Please press E for encryption, or D for decryption: ')

    if choice.upper() == 'E':
        ss_encr()
    elif choice.upper() == 'D':
        ss_decr()
'''
class Key:
    def __init__(self):
        self.alphabet = string.ascii_lowercase

    def key_gen(self):
        self.key = ''.join(random.sample(self.alphabet,len(self.alphabet)))
        return self.key
    
class Cipher:
    def __init__(self,choice):
        self.text = input('Enter your text: ').lower()
        self.string = ''
        self.alphabet = Key().alphabet
        self.choice = choice
        if self.choice == 'E':
            self.key = Key().key_gen()
        elif self.choice == 'D':
            self.key = input('Enter your key: ')

    def ss_encr(self):
        for letter in self.text:
            if letter in self.alphabet:
                self.string += self.key[self.alphabet.find(letter)]
            else:
                self.string += letter

        print(f'Your encryption key is {str(self.key)}. Please keep it safe!')
        print(f'Your encrypted text: {str(self.string)}')
    
    def ss_decr(self):
        for letter in self.text:
            if letter in self.key:
                self.string += self.alphabet[self.key.find(letter)]
            else:
                self.string+= letter

        print(f'Your decrypted text: {str(self.string)}')
        
class Simple:
    def __init__(self):
        self.choice = input('Please press E for encryption, or D for decryption: ')
        self.cipher = Cipher(self.choice)

    def user_choice(self):
        if self.choice.upper() == 'E':
            self.cipher.ss_encr()
        elif self.choice.upper() == 'D':
            self.cipher.ss_decr()

if __name__ == '__main__':
    simple = Simple()
    simple.user_choice()