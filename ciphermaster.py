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

### Playfair Cipher ###
class Text:
    def __init__(self):
        self.text = input('Enter your text: ').upper().replace(' ','')
        self.digraph = []
        self.group = 0
    
    def diagraph(self):
        for i in range(2, len(self.text), 2):
            self.digraph.append(self.text[self.group:i])
            self.group = i
        self.digraph.append(self.text[self.group:])
        return self.digraph
    
    def fillerletter(self):
        k = len(self.text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if self.text[i] == self.text[i+1]:
                    new_word = self.text[0:i+1] + str('x') + self.text[i+1:]
                    new_word = self.fillerletter(new_word)
                    break
                else:
                    new_word = self.text
        else:
            for i in range(0, k-1, 2):
                if self.text[i] == self.text[i+1]:
                    new_word = self.text[0:i+1] + str('x') + self.text[i+1:]
                    new_word = self.fillerletter(new_word)
                    break
                else:
                    new_word = self.text
        return new_word
    
class KeyTable:
    def __init__(self):
        self.key_letters = []
        self.comp_elements = []
        self.matrix = []

    def generate_table(self, word, list1):
        for i in word:
            if i not in self.key_letters:
                self.key_letters.append(i)
    
        for i in self.key_letters:
            if i not in self.comp_elements:
                self.comp_elements.append(i)
        for i in list1:
            if i not in self.comp_elements:
                self.comp_elements.append(i)
    
        while self.comp_elements != []:
            self.matrix.append(self.comp_elements[:5])
            self.comp_elements = self.comp_elements[5:]
    
        return self.matrix
    
    def search(self,element):
        for i in range(5):
            for j in range(5):
                if(self.matrix[i][j] == element):
                    return i, j
        
class Encrypt:
    def __init__(self,matrix,plaintext):
        self.char1 = ''
        self.char2 = ''
        self.plaintext = plaintext
        self.ciphertext = []
        self.matrix = matrix

    def row_rule(self,matr, e1r, e1c, e2r, e2c):
        if e1c == 4:
            self.char1 = matr[e1r][0]
        else:
            self.char1 = matr[e1r][e1c+1]
    
        if e2c == 4:
            self.char2 = matr[e2r][0]
        else:
            self.char2 = matr[e2r][e2c+1]
    
        return self.char1, self.char2

    def column_rule(self,matr,e1r,e1c,e2r,e2c):
        if e1r == 4:
            self.char1 = matr[0][e1c]
        else:
            self.char1 = matr[e1r+1][e1c]
    
        if e2r == 4:
            self.char2 = matr[0][e2c]
        else:
            self.char2 = matr[e2r+1][e2c]

    def rectangle_rule(self,matr, e1r, e1c, e2r, e2c):
        self.char1 = matr[e1r][e2c]
    
        self.char2 = matr[e2r][e1c]
    
        return self.char1, self.char2
    
    def encryptByPlayfairCipher(self):
        for i in range(0, len(self.plaintext)):
            c1 = 0
            c2 = 0
            ele1_x, ele1_y = KeyTable.search(self.matrix, self.plaintext[i][0])
            ele2_x, ele2_y = KeyTable.search(self.matrix, self.plaintext[i][1])
    
            if ele1_x == ele2_x:
                c1, c2 = self.row_rule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)
                # Get 2 letter cipherText
            elif ele1_y == ele2_y:
                c1, c2 = self.column_rule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.rectangle_rule(self.matrix, ele1_x, ele1_y, ele2_x, ele2_y)
    
            cipher = c1 + c2
            self.ciphertext.append(cipher)
        return self.ciphertext

class Decrypt:
    def __init__(self):
        self.char1 = ''
        self.char2 = ''

    def row_rule(self,matr, e1r, e1c, e2r, e2c):
        if e1c == 4:
            self.char1 = matr[e1r][0]
        else:
            self.char1 = matr[e1r][e1c+1]
    
        if e2c == 4:
            self.char2 = matr[e2r][0]
        else:
            self.char2 = matr[e2r][e2c+1]
    
        return self.char1, self.char2

    def column_rule(self,matr,e1r,e1c,e2r,e2c):
        if e1r == 4:
            self.char1 = matr[0][e1c]
        else:
            self.char1 = matr[e1r+1][e1c]
    
        if e2r == 4:
            self.char2 = matr[0][e2c]
        else:
            self.char2 = matr[e2r+1][e2c]        

    def rectangle_rule(self,matr, e1r, e1c, e2r, e2c):
        self.char1 = matr[e1r][e2c]
    
        self.char2 = matr[e2r][e1c]
    
        return self.char1, self.char2

class Playfair:
    def __init__(self):
        self.text = Text()
        self.text.diagraph()
        self.text.fillerletter()

        self.choice = input('Please press E for encryption, or D for decryption: ')
        if self.choice.upper() == 'E':
            self.cipher = Encrypt()
        elif self.choice.upper() == 'D':
            self.cipher = Decrypt()

if __name__ == __main__:
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1]+'z'
    
    print("Key text:", key)
    key = toLowerCase(key)
    Matrix = generate_table(key, list1)