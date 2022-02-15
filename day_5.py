#loops:

#for loop:

#average height of students:
height=[152,145,159,186,195,126,111,125]
sum=0
for i in height:
    sum=sum+i
print(sum/len(height))

scores=[152,145,159,286,195,126,111,125]
highest=0
for i in scores:
    if i>highest:
       highest=i
print(highest) 

#range function and for loop:
# range(start{inclusive},stop{exclusive},skip)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
sum=0
for i in range(2,101,2):
    sum+=i
print(sum)

#FizzBuzz
print('__________________________________________________________')
for i in range(1,101):
    if i %3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

#password generator:
import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=[',','<','>',':',';','?','/','{','}','|',']','[']
password=[]
num=int(input('no of charcters in password: '))
no=int(input('no of numbers in password: '))
sym=int(input('no of symbols in password: '))
l=num-no-sym

for i in range(no):
    password.append(numbers[random.randint(0,len(numbers)-1)])
    print(password)
for i in range(sym):
    password.append(symbols[random.randint(0,len(symbols)-1)])
    print(password)
for i in range(l):
    password.append(letter[random.randint(0,len(letter)-1)])
    print(password)
p=''
for i in range(len(password)):
    a=random.randint(0,len(password)-1)
    p=p+password.pop(random.randint(0,a))
print('your password is: ',p)