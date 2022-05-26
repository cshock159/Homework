import string
import random
import sys

from time import sleep

def setup():
    global allones
    global allzeros
    global randomstring
    global length
    #length = int(sys.argv[1])
    length = int(input("How many numbers deep do you want to go? "))
    randomstring = ''.join([random.choice(string.digits[:2]) for item in range(length)])
    allzeros = ''.join([random.choice(string.digits[0]) for item in range(length)])
    allones = ''.join([random.choice(string.digits[1]) for item in range(length)])
    randomstring = list(randomstring)
    return randomstring, allzeros, allones

def runthrough(priorchar, currentchar, nextchar):
    while currentchar <= length:
        nonstopticker = 0
        # when restarting the search through string
        if currentchar == 0:
            currentThree = randomstring[-1] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
        #Where NEXTCHAR goes into out of index. In 5, here prior is 3, current is 4, and next is 5(Out of index)
        if priorchar == (length - 2):
            nextchar = 0
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)  
        #Max Limit (I.E. 5 - 1 = 4 is the max index)        
        if priorchar == (length - 1):
            currentchar = 0
            currentThree = randomstring[priorchar] + randomstring[0] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
            priorchar = -1
        # Generic Catch all.
        elif currentchar > 0 and currentchar <= (length - 1) and nextchar > 0:
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
        currentchar += 1
        nextchar += 1
        priorchar += 1
        nonstopticker += 1
        if nonstopticker == 1000:
            print("It looks like you've been waiting a while. This may go on to infinity.")
            sleep(10)

def returns(currentThree, currentchar, randomstring):
    global replacement
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
    print("Checking to see if " + randomstring + " is uniform.")
    if randomstring == allones or randomstring == allzeros:
        print(randomstring + " has complete uniformity!")
        exit()
    else:
        print("Not quite uniform yet. Going around with the new number " + randomstring)
        randomstring = list(randomstring)
        return randomstring

def main():
    setup()
    print("Your random character string is: " + ''.join(randomstring))
    sleep(5)
    while 1 == 1:
        currentchar = 0
        nextchar = currentchar + 1
        priorchar = currentchar - 1
        runthrough(priorchar, currentchar, nextchar)


if __name__ == "__main__":
    main()