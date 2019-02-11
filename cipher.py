import sys
import re

print("Please remove any spaces between your characters")
userinput = input("Enter the characters you wish to decode: ")



rot5 = []
result1 = []
rot5 = list(userinput)
base = 48
p = len(rot5)
for z in range(p):
    integer = ord(rot5[z]) - base
    integer = (integer - 5)%10
    integer = integer+base
    answer = chr(integer)
    result1.append(answer)

print("Rot5: " + str(result1))



rot13 = []
result2 = []
rot13 = list(userinput)
base = 97
p = len(rot13)
for z in range(p):
    integer = ord(rot13[z]) - base
    integer = (integer - 13)%26
    integer = integer+base
    answer = chr(integer)
    result2.append(answer)

print("Rot13: " + str(result2))



rot3 = []
result3 = []
rot3 = list(userinput)
base = 97
p = len(rot3)
for z in range(p):
       integer = ord(rot3[z]) - base
       integer = (integer - 3)%26
       integer = integer+base
       answer = chr(integer)
       result3.append(answer)

print("Rot3: " + str(result3))



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

