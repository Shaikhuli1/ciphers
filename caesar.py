# Caesar Cipher
import random

ptext = input('Enter your text: ')
shift = input('Enter the shift you want to use. Enter "RANDOM" if you wish to generate a random one: ')
if shift == 'RANDOM':
    shift = random.randint(1,25)

