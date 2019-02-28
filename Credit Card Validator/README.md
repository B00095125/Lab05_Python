#Credit card#
#Author Andrew Leonard#

This program completes four tasks:
- Verify Card Number
- Determine Card Vendor
- Calculate Checksum of Card Using First Portion.
- Generate a Card

-Verify Card-

The code asks the user to enter a card number and the code will determine if the card is valid or invalid. This process is completed using the luhn algorithm. 
Every odd number in the card number is multiplied by two.
Any numbers over 10 are minused by 9. 
these numbers, and the numbers that were not multiplied by two are then all summed.
mod 10 is then used to check if the card is valid. If this is zero, the card is valid. If it is not zero the card is invalid.   

-Determine Card Vendor-

This was the hardest part of this code to complete. There are a variety of vendors that the card number must be checked against. A series of if statements are used to calculate this portion of the code. The if statements check the beginning portion of the card number. if the first one or two characters equal a certain value, this means they belong to a certain vendor. For example, 34 meant American Express. For larger numbers and ranges, an 'and' was used to check if the first three/four numbers were in a given range. This was how the card vendors were decided. This portion was completed at the end of the code, as an exit function was used to stop the program after a vendor was determined. 

-Checksum- 

The checksum is easy to calculate. The luhn formula is completed the same as the card validator. When this calculation is complete, a number is found. This number is then used to calculate the checksum. If the number is even, for example, 10, the checksum is 0. If not, the number must be minused by 10 in order to get the difference. The difference is what the checksum is. For example, 7 - 10 = -7. This means that the checksum is 7. This is required as a valid card number must have a modulus 10 = 0.  

-Generate- 

The creation of cards was reusing some logic that has previously been used. 
The user is prompted to enter a card vendor they would like, for example: "American Express".
The user must enter the card number correctly, capitals included. 
The code will then assign the vendors signature numbers on, in this case, 34. 
A random 13 numbers will then be generated. This gives a 14 digit number.
At this point, the exact same logic as the previous task is used in order to calculate the checksum. This is the checksum used. 
import random was used to generate the random numbers. The amount of random numbers generated is based on how many numbers are contained in the vendor signature. So this means for a vendor like Discover, 9 random numbers are used.  
