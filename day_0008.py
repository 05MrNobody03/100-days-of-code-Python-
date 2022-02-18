'''
def encode():
    mes=input("enter the message you want to encrypt: ")
    key=int(input('enter the key for encryption: '))
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    en=''
    for i in mes:
        a=arr.index(i)
        en=en+arr[((a+key)%26)]
    return en
def decode():
    mes=input("enter the message you want to encrypt: ")
    key=int(input('enter the key for encryption: '))
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    de=''
    for i in mes:
        a=arr.index(i)
        de=de+arr[((a-key)%26)]
    return de


print("Welcome::")
choice=1
while True:
    choice=int(input("press 1 for encoding and 2 for decoding and 0 to exit: "))

    if choice==1:
        print(encode())
    elif choice ==2:
        print(decode())
    else:
        break


'''

#keyboard arguments vs possitonal argument:

def solve(a,b,c):
    print(a)
    print(b)
    print(c)

print('possitional arguments: ')
solve(1,23,5)
print('keyboard arguments: ')
solve(c=1,a=4,b=85)


# no of cans needed to paint the wall:
import math

def can(height,width,coverage):
    ans=(height*width)/coverage
    if ans%1!=0:
        ans=ans//1 + 1
    return int(ans)

height=float(input('enter the height of the wall: '))
width=float(input('enter the width of the wall: '))
coverage=float(input('enter the coverage of the can: '))

print(f'you will need {can(height,width,coverage)} cans')
