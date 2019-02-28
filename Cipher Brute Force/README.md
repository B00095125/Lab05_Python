#Cipher Brute Forcing Code#
#Author Andrew Leonard#

This code is set to brute force four different cipher types.

- ROT5
- ROT13
- ROT3
- ROT47

The user is prompted to enter the encoded message, with no spaces between any characters. The program will then print out each rotation for each encoding. 
This program uses the same logic for each rotation. The characters and numbers are converted into their ascii number value to be rotated. The numbers are then brought back in relation to zero, in order to make rotation more manageable. 
The numbers are then brought back to their normal value.

each function has a check to make sure that the correct characters are met before rotating. For example, ROT5 will only rotate numbers. Any characters entered will remain the same. 