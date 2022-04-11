from random import randint,randrange


# g = randint(1,99)

print('Hello! Welcome To Number Guessing Game.\nInformation: In this game,Computer will be generate a number and you should guess that number.\nIf number be true you will won.else you will lose.')


print("\n\nAre You Ready? (For Start Press Enter)")

input()

b = 1
s = 0
m = ''
while(b== 1):
    g = randint(1,99)
   
    print('Enter Number: ')
    s = input()
    if s != g:
        print(f'Number not True!\nThe Real Number Is: {g}')
    else:
        print('Perfect.You Won!')
    print('Doyou Want Play Again? Y/N')
    m = input()
    if m == 'Y':
        b = 1
    if m == 'N':
        print('Thank For Play This Game.For Exit Please Press Enter :')
        input()
        b = 2
        

    if m != 'Y' and m != 'N':
        print('You did not enter valid char for start or exit from game. Game will restart again.')


#-------------------- Coded By Benyamin Vala ----------------------------------#


