def my_func():
    print('hello')
    print('Bye')

my_func()

#while loop:

#no=int(input('enter the number of hurdles: '))

import random
no= random.randint(1,10)
while no:
    print(no)
    no-=1

'''
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
    
'''

#hurdle3
'''
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
count=0
while not at_goal():
    if wall_in_front():
        
        turn_left()
        while wall_on_right():
            count+=1
            move()
        turn_right()
        move()
        turn_right()
        while count>0:
            count-=1
            move()
        turn_left()
    else:
        move()
'''

#maze
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        move()
'''
