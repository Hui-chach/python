import random

com = random.randint(1,2)
user = int(input('odd : 1, even : 2\n'))

print('COM(%d) : USER(%d)' %(com, user))
if com == user:
    print('Correct')
else :
    print('Incorrect')
