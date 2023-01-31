# Vigenere Cipher

def vign_encr(): 
    ptext = input('Enter your text: ')
    shift = input('Enter the shift you want to use. Enter "RANDOM" if you wish to generate a random one: ')

def vign_decr():
    ctext = input('Enter your text: ')
    shift = input('Enter the shift you want to use: ')

choice = input('Please press E for encryption, or D for decryption: ')

if choice.upper() == 'E':
    vign_encr()
elif choice.upper() == 'D':
    vign_decr()