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

class Key:
    def __init__(self,text):
        self.keyword = input('Enter the keyword you want to use: ').upper()
        self.keylist = list(self.keyword)
        self.text = text

    def generate_key(self):
        while len(self.keylist) < len(self.text):
            for i in range(len(self.text) - len(self.keylist)):
                self.keylist.append(self.keylist[i])
        return ''.join(self.keylist)

class Cipher: 
    def __init__(self,text):
        self.string = ''
        self.text = text
        self.key = Key(self.text).generate_key()
        self.encr_called = False
        self.decr_called = False
        
    def vig_encr(self):
        for i in range(len(self.text)):
            x = (ord(self.text[i]) + ord(self.key[i])) % 26
            x += ord('A')
            self.string += chr(x)
        self.encr_called = True
        return self.string
    
    def vig_decr(self):
        for i in range(len(self.text)):
            x = (ord(self.text[i]) - ord(self.key[i]) + 26) % 26
            x += ord('A')
            self.string += chr(x)
        self.decr_called = True
        return self.string
    
    def __str__(self):
        if self.encr_called:
            return f'Encrypted text: {self.string}'
        elif self.decr_called:
            return f'Decrypted text: {self.string}'
    
class Vigenere:
    def __init__(self):
        self.text = input('Enter your text: ').upper().replace(' ','')
        self.cipher = Cipher(self.text)
        self.userchoice = input('Please press E for encryption, or D for decryption: ')
    
    def user_choice(self):
        if self.userchoice.upper() == 'E':
            self.cipher.vig_encr()
        elif self.userchoice.upper() == 'D':
            self.cipher.vig_decr()

vigenere = Vigenere()
vigenere.user_choice()
print(str(vigenere.cipher))