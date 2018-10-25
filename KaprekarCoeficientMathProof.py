#import random
import time
#declare global variable
mod1=0
mod2=0
mod3=0
mod4=0
prevResult=0
newResult=0
cnt = 1
def getLower(a1,a2,a3,a4):
    lst=[]
    tempLower = ""
    lst.append(a1)
    lst.append(a2)
    lst.append(a3)
    lst.append(a4)
    lst.sort()
    for i in lst:
        tempLower = tempLower + str(i)
    return int(tempLower)

def getUpper(a1,a2,a3,a4):
    lst=[]
    tempUpper = ""
    lst.append(a1)
    lst.append(a2)
    lst.append(a3)
    lst.append(a4)
    lst.sort()
    lst.reverse()
    for i in lst:
        tempUpper = tempUpper + str(i)
    return int(tempUpper)

def findMods(inputNum):
    #function to get mods and provide lower and bigger 4 digit number
    global mod1
    mod1 = (int(inputNum)%10)
    inputNum = int((int(inputNum) - (int(inputNum)%10))/10)
    global mod2
    mod2 = inputNum%10
    inputNum = int((inputNum - (inputNum%10))/10)
    global mod3
    mod3 = inputNum%10
    inputNum = int((inputNum - (inputNum%10))/10)
    global mod4
    mod4 = inputNum%10

def kaprekarAlgo(numInput):
    findMods(numInput)
    if mod1==mod2==mod3==mod4:
        print("The Number should contains atleast two different digits")
    else:
        lowerNumber=getLower(mod1,mod2,mod3,mod4)
        upperNumber=getUpper(mod1,mod2,mod3,mod4)
        global newResult
        global prevResult
        global cnt
        prevResult = numInput
        newResult = upperNumber-lowerNumber
        if newResult==prevResult:
            print("Kaprekar Constant : "+str(newResult))
            print("Number of Iteration Took : "+str(cnt))
        else:
            cnt = cnt+1
            kaprekarAlgo(newResult)

#randomNum = random.randint(1000,9999)
#randomNum =input("Enter Any Four digit Number : ")
print(time.ctime());
for i in range(1000,10000):
    cnt = 1
    print("Input Number : " + str(i))
    kaprekarAlgo(i)
    #time.sleep(1)
print(time.ctime());