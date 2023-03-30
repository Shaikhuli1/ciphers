# Master script of all the ciphers will be going here, including encryption and decryption
import random
import string

### Simple Substitution ###

class Key:
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.key = ''

    def key_gen(self):
        self.key = ''.join(random.sample(self.alphabet,len(self.alphabet)))

class Cipher:
    def __init__(self):
        self.text = input('Enter your text: ').lower()
        self.string = ''
        self.key = Key().key_gen
        self.alphabet = Key().alphabet

    def ss_encr(self):
        for letter in self.text:
            if letter in self.key:
                self.string += self.key[self.alphabet.find(letter)]
            else:
                self.string += letter

        print(f'Your encryption key is {str(self.key)}. Please keep it safe!')
        print(f'Your encrypted text: {str(self.text)}')
    
    def ss_decr(self):
        for letter in self.text:
            if letter.lower() in self.key:
                self.string += self.alphabet[self.key.find(letter)]
            else:
                self.string+= letter

class Simple:
    def __init__(self):
        self.choice = input('Please press E for encryption, or D for decryption: ')
        self.cipher = Cipher()
        
    def user_choice(self):
        if self.choice.upper() == 'E':
            self.cipher.ss_encr()
        elif self.choice.upper() == 'D':
            self.cipher.ss_decr()

if __name__ == '__main__':
    simple = Simple()
    simple.user_choice()

### Caesar Cipher ###

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

if __name__ == '__main__':
    vigenere = Vigenere()
    vigenere.user_choice()
    print(str(vigenere.cipher))

### One-Time Pad ###

class Key:
    def __init__(self):
        self.text = input('Enter your text: ').upper().replace(' ','')
        self.random_key = ''
        self.length = len(self.text)

    def get_random_string(self):    # Creates a random string of same length as the text entered
        for i in range(self.length):
            self.random_key += random.choice(alphabet)
        return self.random_key

class Cipher:    # Applying One-Time Pad to entered text
    def __init__(self,text,key):
        self.string = ''
        self.text = text
        self.key = key

    def encryption(self):
        for i,char in enumerate(self.text):
            charindex = alphabet.index(char)
            keyindex = alphabet.find(self.key[i])
            cvalue = (charindex + keyindex) % 26

            self.string += alphabet[cvalue]

        print(f'Your encrypted text is {str(self.string)}')
        print(f'Your key is {str(self.key)}. DO NOT SHARE THIS WITH ANYONE OTHER THAN THE RECIPIENT!')

    def decryption(self):
        for i,char in enumerate(self.text):
            charindex = alphabet.index(char)
            keyindex = alphabet.find(self.key[i])
            cvalue = (charindex - keyindex) % 26

            self.string += alphabet[cvalue]

        print(f'Your decrypted text is: {str(self.string)}')

class OTP:   # Controller
    def __init__(self):
        self.key = Key()
        self.text = self.key.text
        self.choice = input('Please press E for encryption, or D for decryption: ')
        if self.choice.upper() == 'E':
            self.keygen = self.key.get_random_string()
        elif self.choice.upper() == 'D':
            self.keygen = input('Enter your key: ')
        
        self.cipher = Cipher(self.text,self.keygen)
    
    def activecipher(self):
        if self.choice.upper() == 'E':
            self.cipher.encryption()
        elif self.choice.upper() == 'D':
            self.cipher.decryption()

if __name__ == '__main__':
    alphabet = string.ascii_uppercase
    otp = OTP()
    otp.activecipher()