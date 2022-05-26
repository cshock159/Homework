import string, random, sys
from time import sleep

def main():
    setup()
    print("Your random character string is: " + ''.join(randomstring))
    sleep(5)
    while 1 == 1:
        currentchar = 0
        nextchar = currentchar + 1
        priorchar = currentchar - 1
        runthrough(priorchar, currentchar, nextchar)

def setup():
    global allones
    global allzeros
    global randomstring
    global length
    global allones
    global allzeros
    global replacement
    length = int(sys.argv[1])
    randomstring = ''.join([random.choice(string.digits[:2]) for item in range(length)])
    allzeros = ''.join([random.choice(string.digits[0]) for item in range(length)])
    allones = ''.join([random.choice(string.digits[1]) for item in range(length)])
    randomstring = list(randomstring)
    return randomstring

def runthrough(priorchar, currentchar, nextchar):
    while currentchar <= length:
        # This resets the nextchar value back to zero, so it will pull the first substring character(digit) in randomstring, completing the loop around.
        if priorchar == (length - 2):
            nextchar = 0
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)  
        # Serves the same purpose as above, but for current character, as well as prior character, after it gets used one last time.       
        if priorchar == (length - 1):
            currentchar = 0
            currentThree = randomstring[priorchar] + randomstring[0] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
            priorchar = -1
        # Everyone else will land here 
        elif currentchar > 0 and currentchar <= (length - 1) and nextchar > 0:
            currentThree = randomstring[priorchar] + randomstring[currentchar] + randomstring[nextchar]
            returns(currentThree, currentchar, randomstring)
        currentchar += 1
        nextchar += 1
        priorchar += 1

def returns(currentThree, currentchar, randomstring):
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
        print("Not quite uniform yet. Going around with the number " + randomstring)
        randomstring = list(randomstring)
        return randomstring

if __name__ == "__main__":
    main()