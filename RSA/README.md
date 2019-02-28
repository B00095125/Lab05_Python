#RSA Challenges#

#Author Andrew Leonard#

- Challenge 1 & 2 -

were essentially completed already, written by Mark Cummins. For challenge 1, nothing was changed. For challenge 2, the ciphertext was just changed in order to decrypt the message. This can be seen on line 30. 

- Challenge 3 -
For this challenge, the python library Cryptodome was needed to be installed. These are libraries are needed in order to use a secret key to extract other key information. The base64 library was also imported, so that the base 64 key could be decoded.
For this code, the secret key that is given is hard coded and saved as pem_key. It is then decoded and saved as key. The function RSA.importkey(key) is used to return RSA key objects. These are important objects such as prime numbers p and q. Futhermore, the public key and n can also be found
These are saved under new variables and n, e, d are printed to the screen. 

- Challenge 4 -
For challenge 4, the exact same logic is used as challenge 3. However, the last part is slightly different and is used to decrypt the ciphertext. The ciphertext given to decrypt is decrypted using the pow function in python. Variables ciphertext, d and n are used in order to decrypt the message. Variables d and n are sourced using the same logic as the previous challenge.  The same code as from challenge 1 and 2 are then used to print the plaintext as a string. 