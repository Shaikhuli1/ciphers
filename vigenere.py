# Vigenere Cipher
'''import string

def generate_key(text,key):
    keylist = list(key)
    while len(keylist) < len(text):
        for i in range(len(text) - len(keylist)):
            keylist.append(keylist[i])
    return ''.join(keylist)

def vign_encr(ptext,key): 
    ctext = ''
    for i in range(len(ptext)):
        x = (ord(ptext[i]) + ord(key[i])) % 26
        x += ord('A')
        ctext += chr(x)
    return ctext
    
def vign_decr(ctext,key):
    ptext = ''
    for i in range(len(ctext)):
        x = (ord(ctext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        ptext += chr(x)
    return ptext

choice = input('Please press E for encryption, or D for decryption: ')
text = input('Enter your text: ').upper().replace(' ','')
keyword = input('Enter the keyword you want to use: ').upper()


if choice.upper() == 'E':
    key = generate_key(text,keyword)
    ctext = vign_encr(text,key)
    print(f'Cipher text: {ctext}')
elif choice.upper() == 'D':
    key = generate_key(text,keyword)
    ptext = vign_decr(text,key)
    print(f'Decrypted text: {ptext}')'''

class Key:
    def __init__(self):
        self.key = input('Enter the keyword you want to use: ').upper()
        self.text = input('Enter your text: ').upper().replace(' ','')
        self.keylist = list(self.key)

    def generate_key(self):
        while len(self.keylist) < len(self.text):
            for i in range(len(self.text) - len(self.keylist)):
                self.keylist.append(self.keylist[i])
        return ''.join(self.keylist)

class Cipher: 
    def __init__(self):
        pass

class Vigenere:
    def __init__(self):
        pass