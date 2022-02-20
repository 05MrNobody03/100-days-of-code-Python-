#day 12 : Namespaces and scope:


#scope:

from hashlib import new


enemies=1

def inc_enemies():
    # enemies=1
    # enemies+=1
    print(f'enemies= {enemies}')

inc_enemies()
print(f'enemies= {enemies}')

def drink():
    potion=2
    print(f'potion = {potion}')

# print(potion) # this line will give error as the variable has local scope

#namespace is a system that keep record of the scope of names of variables

# no block scope:
# local scope is only for functions and methods not some simple intended block 
level=1
em=['zombies','skeleton','mummy']
if level<5:
    new_em=em[0]

print(new_em)

print('__________________________________________')
enemies=1
def battle():
#     enemies += 1
#     print(enemies)
    global enemies
    enemies+=1
    print(enemies)

battle()

print('__________________________________________')

#number guess game:
import random
num=random.randint(1,100)
print('Welcome to the number guess game: ')

def guess(chances,num):
    while chances!=0:
        n=int(input(f'You are left with {chances}: enter the number: '))
        if n==num:
            print("Congrats You guessed it right")
            break
        elif n>num:
            print('Too High')
            chances-=1
        else: 
            print('Too Low')
            chances-=1
    if chances==0:
        print(f"You lost, the correct number was: {num}")
diff=input('choose difficult level: Easy, Medium, Hard: ')
if diff=="Easy":
    guess(10,num)
else:
    guess(5,num)
