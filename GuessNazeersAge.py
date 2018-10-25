import random

NAge = random.randint(20,35)
def CheckAge(Nage):
    for i in range(4):
        num = input("Attempt Left :" + str(3-i) + " - Guess Nazeer's Age : " )
        if Nage == int(num):
            print("You guessed right")
            exit()
        else:
            if i==3:
                print("No Attempts left. Only God Knows his age ")
            else:
                if Nage > int(num):
                    print("Are you kidding. He is Older than " + num)
                else:
                    print("Though he looks old but he is younger")

CheckAge(NAge)