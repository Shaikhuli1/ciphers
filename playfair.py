import random
import string

'''def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
 
        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word
 
 
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)
 
    self.comp_elements = []
    for i in key_letters:
        if i not in self.comp_elements:
            self.comp_elements.append(i)
    for i in list1:
        if i not in self.comp_elements:
            self.comp_elements.append(i)
 
    matrix = []
    while self.comp_elements != []:
        matrix.append(self.comp_elements[:5])
        self.comp_elements = self.comp_elements[5:]
 
    return matrix

def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j

def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]
 
    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]
 
    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]
 
    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]
 
    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
 
    char2 = ''
    char2 = matr[e2r][e1c]
 
    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])
 
        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            # Get 2 letter cipherText
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
 
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def decrypt():
    pass

if __name__ == "__main__":
    text = input('Enter your text: ')
    choice = input('Please press E for encryption, or D for decryption: ')

    if choice == 'E':
        encrypt()
    elif choice == 'D':
        decrypt()'''

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
        self.textinput = Text()
        self.textinput.diagraph()
        self.textinput.fillerletter()

        self.choice = input('Please press E for encryption, or D for decryption: ')
        if self.choice.upper() == 'E':
            self.cipher = Encrypt()
        elif self.choice.upper() == 'D':
            self.cipher = Decrypt()

if __name__ == '__main__':
    playfair = Playfair()
    if len(playfair.textinput.text) != 2:
        playfair.textinput.text[-1] = playfair.textinput.text[-1]+'z'
    
    print("Key text:", key.lower())
    Matrix = generate_table(key, list1)