from random_word import RandomWords

def encryption(text,key):
    pass

def decryption(text,key):
    pass

if __name__ == '__main__':
    text = input('Enter your text: ')
    word = RandomWords()

    while len(word) != len(text):
        word.get_random_word()
    
    choice = input('Please press E for encryption, or D for decryption: ')
    
    if choice.upper() == 'E':
        encryption(text,word)
    elif choice.upper() == 'D':
        decryption(text,word)