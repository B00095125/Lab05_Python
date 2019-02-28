import sys
import re

#Author Andrew Leonard - Cipher Algorithms

#Ask for user input
print("Please remove any spaces between your characters")
userinput = input("Enter the characters you wish to decode: ")


#ROT5 Algorithm
rot5 = []
result1 = []
rot5 = list(userinput)
base = 48
p = len(rot5)
for z in range(p):
    integer = ord(rot5[z]) - base #turn into ascii value and minus so it is 0
    if integer > 0 and integer < 9: # make sure that its a number inputted
        integer = (integer - 5)%10 #rotate and modulus 10
        integer = integer+base # add it back so that it will have a correct value when converted
        answer = chr(integer) #Convert back to int
        result1.append(answer) #add it to the list
    else:
        result1.append(rot5[z]) #if it is a character and not a number, just add it to the list as is
print("Rot5: " + str(result1)) #print



rot13 = []
result2 = []
rot13 = list(userinput)
base = 97
p = len(rot13)

#lowercase characters
for z in range(p):
    if ord(rot13[z]) >= 97 and ord(rot13[z]) <= 122: #check to see if it is a capital or lowercase letter
        integer = ord(rot13[z]) - base #lowercase so minus by base - 97
        integer = (integer - 13)%26 #rotate -13
        integer = integer+base #add back
        answer = chr(integer) #convert to char
        result2.append(answer) #add to list
    elif ord(rot13[z]) >= 65 and ord(rot13[z]) <= 90: #check to see if it is uppercase
        integer = ord(rot13[z]) - 65 #minus to get to zero
        integer = (integer - 13)%26
        integer = integer+65
        answer = chr(integer)
        result2.append(answer)
    else: #this is for anything that was not a character, ie a number
        result2.append(rot13[z])

print("Rot13: " + str(result2))


#caesar cipher - exact same logic as rot13
rot3 = []
result3 = []
rot3 = list(userinput)
base = 97
p = len(rot3)
for z in range(p):
    if ord(rot13[z]) >= 97 and ord(rot13[z]) <= 122:
       integer = ord(rot3[z]) - base
       integer = (integer - 3)%26
       integer = integer+base
       answer = chr(integer)
       result3.append(answer)

    elif ord(rot13[z]) >= 65 and ord(rot13[z]) <= 90:
        integer = ord(rot13[z]) - 65
        integer = (integer - 3)%26
        integer = integer+65
        answer = chr(integer)
        result3.append(answer)
    else:
        result3.append(rot13[z])

print("Rot3: " + str(result3))


#rot47 exact same logic as other 2, except no need for checks as all 47 chars are used.
rot47 = []
result4 = []
rot47 = list(userinput)
#print(rot47)
base = 32
p = len(rot47)
for z in range(p):
    integer = ord(rot47[z]) - base
    integer = (integer - 47)%94
    integer = integer+base
    answer = chr(integer)
    result4.append(answer)

print("Rot47: " + str(result4))

