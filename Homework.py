from asyncio.windows_events import NULL
import string
import random
import time
import sys

from time import sleep

sys.setrecursionlimit(50000)
length = int(input("How many numbers deep do you want to go? "))
randomstring = ''.join([random.choice(string.digits[:2]) for item in range(length)])
allzeros = ''.join([random.choice(string.digits[0]) for item in range(length)])
allones = ''.join([random.choice(string.digits[1]) for item in range(length)])
randomstring = list(randomstring)

currentchar = 0
nextchar = currentchar + 1
priorchar = currentchar - 1

def runThrough():
    global currentchar
    global nextchar
    global priorchar
    while currentchar <= length:
        # when restarting the search through string
        if currentchar == 0:
            print(str(priorchar) + str(currentchar) + str(nextchar) + " in third Slot")
            currentThree = randomstring[-1] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
        #Where NEXTCHAR goes into out of index. In 5, here prior is 3, current is 4, and next is 5(Out of index)
        if priorchar == (length - 2):
            nextchar = 0
            print(str(priorchar) + str(currentchar) + str(nextchar) + " in First Slot") 
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)  
        #Max Limit (I.E. 5 - 1 = 4 is the max index)        
        if priorchar == (length - 1):
            currentchar = 0
            print(str(priorchar) + str(currentchar) + str(nextchar) + " in second Slot")
            currentThree = randomstring[priorchar] + randomstring[0] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
            priorchar = -1
        elif currentchar > 0 and currentchar <= 4 and nextchar > 0:
            print(str(priorchar) + str(currentchar) + str(nextchar) + "in last Slot")
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
        currentchar += 1
        nextchar += 1
        priorchar += 1

def returns(currentThree, currentchar, randomstring):
    global replacement
    replacement = ''
    match currentThree:
        case '111':
            replacement = '0'
        case '110':
            replacement = '1'
        case '101':
            replacement = '1'
        case '100':
            replacement = '0'
        case '011':
            replacement = '1'
        case '010':
            replacement = '1'
        case '001':
            replacement = '1'
        case '000':
            replacement = '0'

    randomstring[currentchar] = replacement
    randomstring = ''.join(randomstring)
    check(randomstring)

def check(randomstring):
    print("checking " + randomstring)
    if randomstring == allones or randomstring == allzeros:
        print(randomstring + " Matches the all ones or zeros!")
        sleep(200)
    else:
        print("not quite done yet. Another round with " + randomstring)
        randomstring = list(randomstring)
        return randomstring

done = 0
while done == 0:
    runThrough()


            