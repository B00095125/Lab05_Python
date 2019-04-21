import random

'''
Author: Andrew Leonard - Credit card luhn python script - 17/2/19
'''
#Dictionary for checking card type
Dictionary = {
    34: "American Express",
    300: "Diners Club - Carte Blance"  ,
    36: "Diners Club - International"  ,
    54:"Diners Club - USA & Canada",
    6011:"Discover",
    637:"Instapayment",
    3528:"JCB",
    5018:"Maestro",
    51: "Mastercard" ,
    4: "Visa",
    4026: "Visa Election"

}

#Dictionary for generating card
genCard = {
    "American Express": 34,
    "Diners Club - Carte Blance": 300,
    "Diners Club - International": 36,
    "Diners Club - USA & Canada": 54,
    "Discover":6011,
    "Instapayment":637,
    "JCB":3528,
    "Maestro":5018,
    "Mastercard":51 ,
    "Visa":4,
    "Visa Election":4026

}

#Promt the user to enter number to generate checksum
cardchecker = input("Please enter the first 15 digits of your card number to calculate checksum: ")
if len(cardchecker) != 15:
    cardchecker = input("Please enter the first 15 digits of your card number to calculate checksum: ")

listCheckTwo = []


#does the luhn algorithm, multiplies ever second number in string by 2 and adds it to a list#
for i in range(0, len(cardchecker),2):
        resultOfMultiples = int(cardchecker[i])*2
        listCheckTwo.append(resultOfMultiples)


#-9 to any numbers over 10
for x in range(len(listCheckTwo)):
    if int(listCheckTwo[x]) > 9:
       change = int(listCheckTwo[x]) - 9
       listCheckTwo[x] = change


#sum the numbers in the above list after theyve been minused
numberssumList = sum(listCheckTwo)
testing = []

#adds all the items in the list that havent been multiplied by 2
answer = 0
for s in range(1, len(cardchecker), 2):
        answer = int(cardchecker[s]) + answer

#adds the sum of multiplied numbers to the sum of the other numbers %10
sumTest = (answer + numberssumList)%10

#if the result is not 0, then we need to minus 10 to get the difference
if sumTest != 0:
    sumTest -= 10
#if it isnt zero, we print out the value
if sumTest != 0:
    print("Check sum is " + str(abs(sumTest)))
#otherwise we can presume it is zero
else:
    print("Check sum is: Zero")

#prompt user to see what card they would like
pickacard = input("Pick what type card you would like: ")
genisis = []
#same logic used for all cards
##Generate American Express Card
if pickacard == "American Express":
    print("Card start: " + str(genCard["American Express"]))#prints the first numbers of the card for each type chosen
    card = []
    for i in range(13):#loops 13 times
        number = random.randint(1, 9) ##picks 13 random numbers to make up the bulk of the card. It is 13 in American Express' case
        #as its starting number is 34, and we need 1 space for the checksum. thus 16 - 3 = 13.
        card.append(number)#add number to the list.

    card.insert(0, 4)
    card.insert(0, 3)##add 34 to the start of the card

##the same logic has been used for every card generated. Only differences are the amount of
#random number generated. This is based on the vendor starting length.

##Generate Diners Club Card
if pickacard == "Diners Club - Carte Blance":
    print("Card start: " + str(genCard["Diners Club - Carte Blance"]))
    card = []
    for i in range(12):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 0)
    card.insert(0, 0)
    card.insert(0, 3)

##Generate Diners Club Card
if pickacard == "Diners Club - International":
    print("Card start: " + str(genCard["Diners Club - International"]))
    card = []
    for i in range(13):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 6)
    card.insert(0, 3)

##Generate Diners Club Card
if pickacard == "Diners Club - USA & Canada":
    print("Card start: " + str(genCard["Diners Club - USA & Canada"]))
    card = []
    for i in range(13):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 4)
    card.insert(0, 5)

#Generate Discover Card
if pickacard == "Discover":
    print("Card start: " + str(genCard["Discover"]))
    card = []
    for i in range(11):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 1)
    card.insert(0, 1)
    card.insert(0, 0)
    card.insert(0, 6)

#Generate Instapayment card
if pickacard == "Instapayment":
    print("Card start: " + str(genCard["Instapayment"]))
    card = []
    for i in range(12):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 7)
    card.insert(0, 3)
    card.insert(0, 6)

#generate JCB Card
if pickacard == "JCB":
    print("Card start: " + str(genCard["JCB"]))
    card = []
    for i in range(11):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 8)
    card.insert(0, 2)
    card.insert(0, 5)
    card.insert(0, 3)

#Generate Maestro Card
if pickacard == "Maestro":
    print("Card start: " + str(genCard["Maestro"]))
    card = []
    for i in range(11):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 8)
    card.insert(0, 1)
    card.insert(0, 0)
    card.insert(0, 5)

#Generate Mastercard
if pickacard == "Mastercard":
    print("Card start: " + str(genCard["Mastercard"]))
    card = []
    for i in range(13):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 1)
    card.insert(0, 5)

#Generate Visa
if pickacard == "Visa":
    print("Card start: " + str(genCard["Visa"]))
    card = []
    for i in range(14):
        number = random.randint(1, 9)
        card.append(number)

    card.insert(0, 4)

#Generae Visa Election
if pickacard == "Visa Election":
    print("Card start: " + str(genCard["Visa Election"]))
    card = []
    for i in range(11):
        number = random.randint(1, 9)
        card.append(number)
    card.insert(0, 6)
    card.insert(0, 2)
    card.insert(0, 0)
    card.insert(0, 4)

card1 = ''.join(str(e) for e in card)

###CALCULATIONS TO CALCULATE THE CHECKSUM AND ADD IT TO THE END###

#Does same calculations as before, does the luhn algorithm#
for i in range(0, len(card1),2):
        resultOfMultiples = int(card1[i])*2
        genisis.append(resultOfMultiples)


#Loop through the odd numbers and -9 to any over 10
for x in range(len(genisis)):
    if int(genisis[x]) > 9:
       change = int(genisis[x]) - 9
       genisis[x] = change


#sum any numbers in the above list
numberssumList = sum(genisis)
testing = []

#adds all the items in the list
answer = 0
for s in range(1, len(card1), 2):
        answer = int(card1[s]) + answer


sumTest = (answer + numberssumList)%10

if sumTest != 0:
    sumTest -= 10

checksum = abs(sumTest)
print("Newly Generated Card: "+str(card1)+str(checksum)) ##Prints the new card number with the checksum at the end

##prompts user to enter the card number to be checked if valid
cardNumber = input("Please enter your card number to be checked: ")

listCheck = []


#Check if the number is correct syntax
if len(cardNumber) != 16:
        test = input("The card number must be 16, please try again: ")




#Loop through the card, and multiply every second int.
for i in range(0, len(cardNumber),2):
        resultOfMultiples = int(cardNumber[i])*2
        listCheck.append(resultOfMultiples)

#print("This is the list of odd numbered multiplied by 2: " + str(listCheck))

#Loop through the odd numbers and -9 to any over 10
for x in range(len(listCheck)):
    if int(listCheck[x]) > 9:
       change = int(listCheck[x]) - 9
       listCheck[x] = change

#print("any numbers greater than 9 are minused by 9: " + str(listCheck))

#sum any numbers in the above list
numberssumList = sum(listCheck)
#print("Sum of above list: " + str(numberssumList))
testing = []

answer = 0
for s in range(1, len(cardNumber), 2):
        answer = int(cardNumber[s]) + answer

#Adds the sum of the numbers together

#checks if the card is valid or invalid
answer = answer + numberssumList
if answer%10 == 0:
    print("Card is valid") #card is valid if mod 10 is 0
if answer%10 != 0:
    print("Card is not valid")

##If Statements check if the first part of the number match the vendor type
##for numbers too large, a range with 'and' was used to check the number.
##The program uses the top dictionary to print the vendor type, and then exits the program with exit()
if int(cardNumber[0]) == 3:
    #Check if american express
    if int(cardNumber[0:2]) == 34 or int(cardNumber[0:2]) == 37:
        print(Dictionary[34])
        exit()
    #Diner club International
    elif int(cardNumber[0:2]) == 36:
        print(Dictionary[36])
        exit()
    #Diner club - Carte Blanche
    elif cardNumber[0:3] == 300 or int(cardNumber[0:3]) <= 306:
        print(Dictionary[300])
        exit()
    #JCB
    elif int(cardNumber[0:4]) >= 3528 and int(cardNumber[0:4]) <= 3589:
        print(Dictionary[3528])
        exit()

if int(cardNumber[0]) == 4:
    #Visa Election
    if int(cardNumber[0:4]) == 4026 or int(cardNumber[0:4]) == 4508 or int(cardNumber[0:4]) == 4844 or int(cardNumber[0:4]) == 4913 or int(cardNumber[0:4]) == 4917 or int(cardNumber[0:6]) == 417500:
        print(Dictionary[4026])
        exit()
    else:
        #VISA
        print(Dictionary[4])
        exit()

if int(cardNumber[0:2]) == 54:
    #Diners club USA OR CANADA
    print(Dictionary[54])
    print("or")
    print(Dictionary[51])
    exit()

#Instapayment
if int(cardNumber[0:3]) == 637 or int(cardNumber[0:3]) == 638 or int(cardNumber[0:3]) == 639:
    print(Dictionary[637])
    exit()

#Mastercard
if int(cardNumber[0:2]) == 51 or int(cardNumber[0:2]) == 52 or int(cardNumber[0:2]) == 53 or int(cardNumber[0:2]) == 54 or int(cardNumber[0:2]) == 55 or int(cardNumber[0:6]) > 222099 and int(cardNumber[0:6]) < 272100:
    print(Dictionary[51])
    exit()

#Discover
if int(cardNumber[0:3]) == 644 or int(cardNumber[0:3]) == 649 or int(cardNumber[0:4]) == 6011 or int(cardNumber[0:2]) == 65 or int(cardNumber[0:6]) > 622125 and int(cardNumber[0:6]) < 622926:
    print(Dictionary[6011])
    exit()

#Maestro
#Since as there are no other options, will presume it is maestro
else:
    print(Dictionary[5018])




