#debugging 

# grace hopper found first bug
# a moth found in her relay in her computer
# 1) Describe the problem: make sence of the problem and understand it yourself

def my_func():
# function loops through a range of values and then prints when a particular value if encountered
# here it is 20
    # for i in range(1,20):
# i reaches 20 and then it prints 
    for i in range(1,21):
    #    print(i)                  #to check the i values
#i never reaches to 20 as it is excluding 20 

        if i==20:
            print("You got it")

my_func()

print('______________________________________________')

from random import randint
dice_img=['1one','2two','3three','4four','5five','6six']
# 1 and 6 are included dice_num=randint(1,6)
dice_num=randint(0,5)
print(dice_img[dice_num])

print('______________________________________________')

year=int(input('enter your year of birth: '))
if year>1980 and year<=1994:               # year 1994 is not included in this statement
    print('yuor are a millenial')
elif year>1994:
    print('you are a gen-z')

print('______________________________________________')

age=int(input('enter your age: '))
if age>18:
    print(f'you can drive at age {age}')

print('______________________________________________')

pages=0
words=0
pages=int(input('enter no of pages: '))
words=int(input('enter number of words per page: '))
total=pages*words
print(total)

print('______________________________________________')
# debugger::
# use debugger to solve and identify the bugs