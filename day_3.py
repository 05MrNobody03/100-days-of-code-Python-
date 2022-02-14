#conditional statements:


#import this

'''
if condition:
    do this
else:
    do this

'''

print("__________________________________________________________")
water_level=50
if water_level>=80:
    print("Drain the water")
else:
    print("continue")

print("__________________________________________________________")
#roler coster ride:
#height>120cm
#age>15
'''
height=int(input("enter your height in cms: "))
age=int(input("Enter your age: "))

if height>120 and age>15:
    print('your are allowed to ride the roller coster')
else:
    print("Sorry you are not allowed to ride the roller coster")
'''
# relational operators:
''' 
> greater than
< less than
>= greater than equal too
<= less than equal too
== equality
'''

print("__________________________________________________________")
# even and odd exercise:
'''
num=int(input("enter a number: "))
if num%2==0:
    print('even')
else:
    print("odd")
'''
#nested loop:

print("__________________________________________________________")
'''
height=int(input("enter your height in cms: "))
age=int(input("Enter your age: "))

if height>120 and age>15:
    print('your are allowed to ride the roller coster')
    if age>18:
        print('please pay 12$ for the ride')
    else: 
        print('please pay 7$ for the ride')
else:
    print("Sorry you are not allowed to ride the roller coster")
'''

print("__________________________________________________________")
#upgraded BMI calculator

height=float(input('enter your height: '))
weight=float(input('enter your weight: '))

bmi=weight/height**2
print('BMI = ',bmi)
if bmi<18.5:
    print('underweight!')
elif bmi>=18.5 and bmi<25:
    print('normal weight')
elif bmi>=25 and bmi<30:
    print('obese')
elif bmi>=30 and bmi<35:
    print('clinically obese')
else:
    print("mar gaya *********  la la..... lalla la la la lalla la la....")

# leap year

print("__________________________________________________________")
year=int(input('Enter a year: '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print('not leap year')
    else:
        print('leap year')
else:
    print('not leap year')

#pizza order pizza:
# size, pepperoni, cheese
print("__________________________________________________________")
pizza_size=input("enter the size of pizza you want? S, M, L? ")
pepproni=input('do you want pepproni? Y, N? ')
cheese=input('do you want cheese? ')
bill=0
if pizza_size=="S":
    bill+=15
    if pepproni=="Y":
        bill+=2
elif pizza_size=="M":
    bill+=20
    if pepproni=="Y":
        bill+=3
elif pizza_size=="L":
    bill+=25
    if pepproni=="Y":
        bill+=3

if cheese=='Y':
    bill+=1

print("Your final bill is:",bill)


print("__________________________________________________________")

#logical operators:
# and, or ,not

# true love calculator:

str1= input("enter your name: ")
str2= input('enter her name: ')

str1=str1.lower()
str2=str2.lower()

l=str1.count('t')+str2.count('t')+str1.count('u')+str2.count('u')+str1.count('r')+str2.count('r')+str1.count('e')+str2.count('e')

r=str1.count('l')+str2.count('l')+str1.count('o')+str2.count('o')+str1.count('v')+str2.count('v')+str1.count('e')+str2.count('e')

print("your love percentage is",int(l)*10+int(r))

# Adventure game:
print("-:Welcome to the treasure island:-")
if input('you want to go left or right: ')=="left":
    if input('you have reached a river: now you want to swim or wait?') == 'wait':
        if input(' you have 3 doors in front of you, red, yellow, blue, which one will you choose: ')=='yellow':
            print('you found the treasure!!!')
        else:
            print("Game Over")
    else:
            print("Game Over")
else:
            print("Game Over")