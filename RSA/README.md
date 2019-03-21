#RSA Challenges#

#Author Andrew Leonard#

- Challenge 1 & 2 -

These were essentially completed already, written by Mark Cummins. For challenge 1, nothing was changed. For challenge 2, the ciphertext was just changed in order to decrypt the message. This can be seen on line 30. 

- Challenge 3 -
For this challenge, the python library Cryptodome was needed to be installed. These are libraries are needed in order to use a secret key to extract other key information. The base64 library was also imported, so that the base 64 key could be decoded.
For this code, the secret key that is given is hard coded and saved as pem_key. It is then decoded and saved as key. The function RSA.importkey(key) is used to return RSA key objects. These are important objects such as prime numbers p and q. Futhermore, the public key and n can also be found
These are saved under new variables and n, e, d are printed to the screen. 

- Challenge 4 -
For challenge 4, the exact same logic is used as challenge 3. However, the last part is slightly different and is used to decrypt the ciphertext. The ciphertext given to decrypt is decrypted using the pow function in python. Variables ciphertext, d and n are used in order to decrypt the message. Variables d and n are sourced using the same logic as the previous challenge.  The same code as from challenge 1 and 2 are then used to print the plaintext as a string. 

- Challenge 5 - 
For this challenge, the user is given multiple variables. The variables include p, q, dp, dq, pinv, qinv, n and the ciphertext. The aim of this challenge is to solve for the ciphertext. The extra variables are sometimes used in RSA in order to speed up the process. https://www.rootnetsec.com/picoctf-weird-rsa/ provides a sufficient algorithm in order to solve for this cipher. This algorithm takes advantage of the chinese remainder theory. four new variables are created and aid in the solving of the cipher, mOne, mTwo, h and m. the variable m is then found and is converted to a string as the flag is revealed. 

- Challenge 6 - 
In challenge 6, the user is given some variables. These variables are e, p, q, c and n. The user must solve for d. D is the private key used to decrypt RSA messages. As a result, an inverse mod function is used in order to solve for d. A function is needed in this case as the float is too big otherwise. This is the Euclidean algorithm. A variable phi is created and assigned the value (p-1)*(q-1). Thus, to solve for d, the mod inverse of e and phi must be found. Once d is found, the user now has all the requirements in order to decrypt the ciphertext.

- Challenge 7 -
This challenge is similar to challenge 6, however the user is only given n. Thus, the user must find the values for p and q to solve for d. This is made possible by importing the factorDB API sourced from github. Source: https://github.com/ryosan-470/factordb-pycli?fbclid=IwAR2SYJCiizMXWOvHrmvZqKLTmT0rEhm1Tl7dYcBrJ_oRN8vSXqIxFGrQuB8. This API allows the user to factorise the number n and print out the values. The values were then printed to the console, and hard coded into the program as p and q respectively. n is a prime number, so factor db only finds 2 numbers when factorising it. 
Once p and q is found, the exact same logic is used in order to solve for c using the Euclidean algorithm.

- Challenge 8 -
The user is given values n, e and c. This would not be solveable if e was a large number. This challenge is solveable if e is a very low number. This is based on the logic of M^e < n. If this is true, then M is not encrypted. therefore, c = M^e. By this logic, the program can find c if it finds the cubed root of the ciphertext. The function used to find the cubed root of the ciphertext in this program was sourced from: https://stackoverflow.com/questions/52313392/compute-cube-root-of-extremely-big-number-in-python3
This function allows for the cubed root of very big numbers, however one must be added to the end in order to make up for rounding down. The program will then convert this ciphertext to string to find the flag. This is because the RSA did not encrypt the ciphertext as e was too small.

- Challenge 9 -
In this challenge, the user is given multiple values, e1,e2,e3, n1,n2,n3 and c1,c2,c3. The logic for this solution is similar to challenge 8. However this is solved by using Gauss's algorithm. This algorithm was sourced from: https://www.di-mgt.com.au/crt.html?fbclid=IwAR2fNqFHj06r7AoZOY2sxCF-t77VpcDxfknzDpsuo8egG-9PCLwoKhTUmm0. m can be recovered by finding the cube root of x. X is found through the following formula. All n values are multiplied together, called nMultiplied. test1 = n2*n3, test2 = n3*n1 and test3 = n2*n1. These values are then mod inversed. d1= modInverse(test1, n1),  d2= modInverse(test2, n2) and d3= modInverse(test3, n3). X is the sum of c1*test1*d1 + c2+test2+d2 + c3+test3+d3. X is then multiplied by nMultiplied. This value is then cube rooted and converted to string. This results in the flag being revealed. Again, this solution takes advantage of m^e < n. 

- Challenge 10 -
This challenge uses the exact same logic as 8 and 9. The e value is too small in this case, which makes decrypting the ciphertext easier. The user is given three values, n1, n2, e1, e2, c1, c2. Immediately it is noticeable that e2 is a very small number, making it vulnerable to the m^e < n attack. The same logic as applied to 8 is applied to e2 and c2 and thus the flag is revealed.  
