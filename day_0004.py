#day 4
# randomization and python lists
# random module
import random
random_int=random.randint(1,10)
print(random_int)

# module is a script that can be used in your code which is developed seperately

#ransom float
print(random.randint(1,5)+random.random())

#heads or tails
num=input('heads or tails: ')
n=random.randint(0,1)
if num=='heads':
    if n==0:
        print("you guessed it right")
    else:
        print('better luck next time') 
else:
    if n==1:
        print("you guessed it right")
    else:
        print('better luck next time') 

#python list:
lst=['h2r','hustler','devil']
print(lst[0],lst[1],lst[2],lst[-1],lst[-2])
        
lst.append('132')
print(lst)

#who is going to pay the bill 
names=input()
names=names.split(', ')
sel=random.randint(0,len(names)-1)
print(f'{names[sel]} is going to pay the bill today')

#treasure map
r1=['0','0','0']
r2=['0','0','0']
r3=['0','0','0']

map=[r1,r2,r3]

print(f'{r1}\n{r2}\n{r3}')
treasure=input('where you want to keep your treasure: ')
map[int(treasure[0])][int(treasure[1])]='x'
print(f'{r1}\n{r2}\n{r3}')

#rocks papers and scissors:

num=int(input(' enter 0 for rock, 1 for paper, 2 for scissors: '))
n=random.randint(0,2)
print(n)
if num==n:
    print('game tie')
elif num==0:
    if n==1:
        print('you lost')
    elif n==2:
        print('you won')
elif num==1:
    if n==2:
        print('you lost')
    elif n==0:
        print('you won')
elif num==2:
    if n==0:
        print('you lost')
    elif n==1:
        print('you won')
