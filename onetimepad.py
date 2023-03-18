#from random_word import RandomWords
import random
import string

'''
def get_random_string(length):
    randstring = ''
    for i in range(length):
        randstring += random.choice(alphabet)
    return randstring

def encryption(text,key):
    ciphertext = ''
    for i,char in enumerate(text):
        charindex = alphabet.index(char)
        keyindex = alphabet.find(key[i])
        cvalue = (charindex + keyindex) % 26

        ciphertext += alphabet[cvalue]

    print(f'Your encrypted text is {ciphertext}')
    print(f'Your key is {key}. DO NOT SHARE THIS WITH ANYONE OTHER THAN THE RECIPIENT!')

def decryption(text,key):
    plaintext = ''
    for i,char in enumerate(text):
        charindex = alphabet.index(char)
        keyindex = alphabet.find(key[i])
        cvalue = (charindex - keyindex) % 26

        plaintext += alphabet[cvalue]

    print(f'Your encrypted text is {plaintext}')

if __name__ == '__main__':
    text = input('Enter your text: ').upper().replace(' ','')

    #word = RandomWords()

    #while len(word) != len(text):
        #word.get_random_word()
    
    choice = input('Please press E for encryption, or D for decryption: ')
    
    if choice.upper() == 'E':
        key = get_random_string(len(text))
        encryption(text,key)
    elif choice.upper() == 'D':
        key = input('Enter your key: ')
        decryption(text,key)
'''

class Key:
    def __init__(self):
        self.text = input('Enter your text: ').upper().replace(' ','')
        self.random_key = ''
        self.length = len(self.text)

    def get_random_string(self):
        for i in range(self.length):
            self.random_key += random.choice(alphabet)

class Cipher:
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

        print(f'Your encrypted text is {str(self.string)}')

class OTP:
    def __init__(self):
        self.keygen = Key()
        self.text = self.keygen.text
        self.choice = input('Please press E for encryption, or D for decryption: ')
        if self.choice.upper() == 'E':
            self.key = self.keygen.get_random_string()
        elif self.choice.upper() == 'D':
            self.key = input('Enter your key: ')
        
        self.cipher = Cipher(self.text,self.key)
    
    def activecipher(self):
        if self.choice.upper() == 'E':
            self.cipher.encryption()
        elif self.choice.upper() == 'D':
            self.cipher.decryption()

if __name__ == '__main__':
    alphabet = string.ascii_uppercase
    otp = OTP()
    otp.activecipher()