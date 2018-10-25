## test Pattern

#    *
#   ***
#  *****
# *******
for i in range(1,5):
    for j in range(1,5-i):
        print(' ',end="")
    for k in range(0,(2*(i-1)+1)):
        print('*',end="")
    print('\n',end="")


#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

for i in range(1,7):
    for j in range(1, 7 - i):
        print(' ', end="")
    for k in range(1,i):
        print("* ",end="")
    print('\n',end="")