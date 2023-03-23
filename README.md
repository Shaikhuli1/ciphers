# Ciphers

A collection of ciphers of the substitution type that will be modelled mathematically were applicable and implemented using Python. Towards the end of this project, the ciphers will be consolidated into a main script that will run using user input.

Currently, the list of ciphers to include and how they work (subject to change) are below:

  * [Simple substitution](http://practicalcryptography.com/ciphers/simple-substitution-cipher/)
  * [Caesar](https://en.wikipedia.org/wiki/Caesar_cipher) 
  * [One-Time Pad](https://www.geeksforgeeks.org/implementation-of-vernam-cipher-or-one-time-pad-algorithm/)
  * [Playfair](https://www.geeksforgeeks.org/playfair-cipher-with-examples/)
  * [Vigenere](https://www.geeksforgeeks.org/vigenere-cipher/)
  * [Hill](https://www.geeksforgeeks.org/hill-cipher/)
  * [Four-Square](http://practicalcryptography.com/ciphers/four-square-cipher/)
  * [RSA Algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

Both encryption and decryption methods should be with each cipher


Note for One-Time Pad -- ideally the key used for this cipher is supposed to be generated completely from random via the use of tools like a hardware random generator. As something like this is not available for use using a simple Python script, absolute security cannot be ensured as the random module used is not classed as truly random. 

Furthermore, once the key is generated and shared to the recipient, it is supposed to be discarded with no trace of it available anywhere. As the script I make technically doesn't do that, another one of the four tenets of the OTP cipher is not fully adhered to.

Note for Four-Square -- while it is possible and a lot easier to apply the pycipher package in order to achieve a working script, I will attempt to make it from scratch.
