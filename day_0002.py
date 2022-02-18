# today's challenge Tip Calculator:
# input no of people
# input total bill
# input percentage of tip

# Primitive datatypes

#yesterday:
#print(len(12352)) # gives type error

#types of datatypes:
# String
# Integer
# Float
# Boolean

# string: string of characters
# "Hello"
#"Hello"[0]
print("hello"[0])
#prints h 
# called subscripting
# starts counting from 0
# to print last character
print("hello"[4])

#int
#123
print(123+345)
print(123_456_789) #same as 123456789

#float: numbers contaning decimal point
print(5.265)

# Boolean: True or False

print(True)
print(False)

# typeerror is like a potato factory making
#  fries is given stone instead of potato 
# to make fries
'''
#type checking
type(123) #o/p will be int
print(str(123))
'''
# str(132) is type conversion just like int(), float() ,etc

# datatype challenge: sum of digits(2 digit no)
'''
num=input("enter a number:")
print('the sum digits is',int(num[0])+int(num[1]))
'''
#mathematical operations 

#addition +
#substraction -
#multiplication *
#division / = always output is float 
#power **
#modulo %  

#power> mul and div

print(3*3+3/3-3) # float as o/p

#BMI Calculator:
# input weight and height
# formula: 
'''
weight=float(input("Enter your weight: "))
height=float(input("enter your height: "))

print("Your BMI is: ",weight/height**2)
'''
# number manipulation and fstring

#print(int(8/3))
print(round(8/3,3)) # round(maths, no of digits to round it)
print(8//3) # floor division
result = 4/2
result/=2
print(result)
# result-=2 => result = result -2

#fstring
print(f'your score= {56} and you won by {56.26}')

# life in weeks: input your age

life=int(input('Enter your age: '))
rem_life=80-life         #assuming an average person lives for 80 years
print(f'your remaining life is about \n{rem_life} years \n{rem_life*52} weeks \n{rem_life*365} days ')

#TIP CALCULATOR:
total=float(input('Enter the total bill: '))
percent=int(input("what percent of tip would you like to give? 10, 12, 15? "))
people=int(input("how many people are going to split the bill: "))
print(f'the tip for {total} bill at {percent}% and among {people} number of people will be {round(total*percent/(100*people),2)} ')

# thats all for the day2
