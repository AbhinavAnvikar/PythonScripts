from itertools import combinations

SevenPart = input("Enter all 7 partitions comma (,) seperated : ");
SevenPart = SevenPart.split(',')
part1 = SevenPart[0];
part2 = SevenPart[1];
part3 = SevenPart[2];
part4 = SevenPart[3];
part5 = SevenPart[4];
part6 = SevenPart[5];
part7 = SevenPart[6];

if ((int(part1)+int(part2)+int(part3)+int(part4)+int(part5)+int(part6)+int(part7))!=100):
    print("Incorrect partition. The sum of all the parts has to be 100")
    exit()
else:
    pass

comb = list(combinations([part1,part2,part3,part4,part5,part6,part7],1))
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],2)):
    comb.append(i)
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],3)):
    comb.append(i)
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],4)):
    comb.append(i)
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],5)):
    comb.append(i)
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],6)):
    comb.append(i)
for i in list(combinations([part1,part2,part3,part4,part5,part6,part7],7)):
    comb.append(i)



for i in range(1,101):
    for j in list(comb):
        sum = 0
        for k in j:
            sum= sum+int(k)
        if sum == i:
            print(str(i) + " Sum Found ")
            fnd = 1
            break
        else:
            pass

    if fnd ==0:
        print( str(i) +" Sum Not Found")
        break
    fnd=0

#for i in list(comb):
#    print(i)
    #sum = 0;
    #for j in i:
    #    sum = sum + j
    #print(sum)