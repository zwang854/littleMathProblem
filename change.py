import random
from begin import Begin

balls = Begin()

print(balls.a)

win = 0
lose = 0
def change():
    i = random.randint(0,1)
    j = random.randint(0,2)

    if j == 0:
        a = 1
    elif j == 1:
        b = 1
    elif j == 2:
        c = 1

    userin = random.randint(0,2)



    if userin == 'a' and a==1:
        win=win+1
    elif userin == 'b' and b==1:
        print('win')
    elif userin == 'c' and c==1:
        print('win')
    else:
        print('loose')
        