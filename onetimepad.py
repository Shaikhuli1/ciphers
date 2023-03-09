#from random_word import RandomWords
import random
import string

def get_random_string(length):
    alphabet = string.ascii_uppercase

    for i in range(length):
        randstring = ''.join(random.choice(alphabet))
    return randstring


def encryption(text,key):
    pass

def decryption(text,key):
    pass

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