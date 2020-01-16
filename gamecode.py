import random
import time
name=input("Please enter your name-:\n")
print(f'''hello {name} \nWelcome to this game created by Raees ;)
This game involves first me thinking of a number and then you trying to guess that number. ''')
while True:
    try :
        wannaPlay=input('Do you wanna play\ntype yes or no\n\n')
        if wannaPlay not in ['yes','no','YES','NO','Yes','No','YEs','nO','YeS','yES']:
            raise TypeError
        break
    except:
        print('Please type either yes or no')

if wannaPlay in ['no','NO','No','nO']:
    print('I am so sorry you did not like my game:( maybe you can drop in some suggestions\n')
    suggestions=input()
else:
    print('Okay so we are in the endgame right now \nJust joking (forgive my pjs) anyways lets continue with the game\n')
    print("now I'll ask you for two things only \n1.First the range that is the upper limit and then the lower limit in which you want me to think the number\n2.Second the number of turns that you'll require to guess that.")
    while True:
        try:
            range1=list(map(int,input('Please give us the lower and upper limits of the range : ').split()))
            if len(range1)!=2:
                raise ValueError
        except:
            print('Please enter only two integers')
        else:
            range1.sort()
            break
    while True:
        try:
            turns=int(input('how may turns do you want?: '))
        except:
            print('please enter an integer only')
        else:
            break
    print('Ok setting up your game')
    count=random.randint(1,6)
    while count!=0:
        print('...')
        count-=1
        time.sleep(.8)
    print('Now we are all set to go')
    number=random.randint(range1[0],range1[1])
    count=0
    print('Best of luck making your guesses ;) ;)')
    while True:
        try:
            guess=int(input())
        except:
            print('please enter only integers')
        else:
            count+=1
            if guess==number:
                print(f'Congrats you won in {count} number of turns')
                break
            elif count==turns:
                print(f'Sorry that was a wrong guess and you have no more chances left\nMy guess was {number}\nBetter luck next time')
                break
            else:
                value=abs(guess-number)
                a=(range1[1]-range1[0])//turns
#                 print(value,a)
                if a//2<value<=a:
                    print(f'No that was a wrong a guess but you are CLOSE\nYou have {turns-count} chances left')
                elif value<=a//2:
                    print(f'Oops that was a wrong guess but you are TOO CLOSE\nYou have {turns-count} chances left')
                else:
                    print(f'No that was a wrong guess\n{turns-count} chances are left')
