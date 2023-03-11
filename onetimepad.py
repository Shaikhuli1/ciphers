#from random_word import RandomWords
import random
import string
alphabet = string.ascii_uppercase

def get_random_string(length):
    for i in range(length):
        randstring = ''.join(random.choice(alphabet))
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
    key = get_random_string(len(text))
    #word = RandomWords()

    #while len(word) != len(text):
        #word.get_random_word()
    
    choice = input('Please press E for encryption, or D for decryption: ')
    
    if choice.upper() == 'E':
        encryption(text,key)
    elif choice.upper() == 'D':
        decryption(text,key)