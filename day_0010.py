'''
#functions with output

def cal():
    result=3*50
    return result

print(cal())

def format_name(f_name,l_name):
    print(f'hello and welcome {f_name + " " + l_name}')

f_name=input('enter your first name: ')
l_name=input('enter your last name: ')

format_name(f_name.title(),l_name.title())

#multiple return values: 

def ret(a,b,c):
    return a*2,b*2,c*2

print(ret(2,3,4))

#no of days in month:
#input the year and no of month

def leap(year):
    """this is a docstring that tells about this function:
        this function take in 1 int paramater and returns
         if the input year is leap year or not"""
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year=int(input('enter the year: '))
month=int(input('enter the month: '))

days=[31,28,31,30,31,30,31,31,30,31,30,31]

leapOrNot=leap(year)
if leapOrNot and month ==2:
    print(days[month-1] +1)
else:
    print(days[month-1])


'''

#calculator program:

import os
def cal(f,op,s):
    if op=='+':
        return f+s
        
    elif op=='-':
        return f-s
    elif op=='*':
        return f*s
    elif op=='/':
        return f/s
    else:
        return "invalid selection"

a='y'
while a=='y':

    f=int(input('enter the first number: '))
    op=input('select the operation: ')
    s= int(input('enter the second number: '))
    result = cal(f,op,s)
    print(result)
    a=input('enter y to continue and n to restart: ')
    while a=='y':
        op=input('select the operation: ')
        s=int(input('enter the second number: '))
        result = cal(result,op,s)
        print(result)
        a=input('enter y to continue and continue to restart and n to exit: ')
    os.system('cls')
    a='y'

