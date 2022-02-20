#higher or Lower
import random
lst=[['ronaldo',403],['kylie jenner',311],['messi',284],['dwayne jhonson',299],['selena gomez',298],['ariana grande',297]]
random.shuffle(lst)
count=0
for i in range(len(lst)-2):
    print(lst[i][0] ,'\nVS',lst[i+1][0])
    hrl=input('higher or lower: ')
    if hrl=='higher' and lst[i+1][1]>lst[i][1]:
        count+=1
        print('Correct!')
        print(f"Your score is: {count}")
    elif hrl=='lower' and lst[i][1]>lst[i+1][1]:
        count+=1
        print('correct')
        print(f"Your score is: {count}")
    else:
        print('wrong')
        break
print('GAME OVER')
print(f'your score is: {count}')