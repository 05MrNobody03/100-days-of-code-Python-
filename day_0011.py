# for _ in range(x):
#     _ is used when you dont need that variable


# Blackjack Capstone Project
import random
import os

def new_card():
    a=cards[random.randint(0,12)]
    b=cards[random.randint(0,12)]
    return a,b

def card_sum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum

play=input('Do you want to play the game of BlackJack? Type y for yes and n for no: ')
J,Q,K=10,10,10
A=1
cards=[1,2,3,4,5,6,7,8,9,10,J,Q,K]
if play=='y':
    print('welcome to the game of BlackJack')
    x,y,z=cards[random.randint(0,12)],cards[random.randint(0,12)],cards[random.randint(0,12)]
    your_cards=[x,y]
    print(your_cards)
    computer_cards=[z]
    print(computer_cards)
    hit=input('type y to get another card and n to pass: ')
    
    while hit=='y' and card_sum(your_cards)<=21:
        a,b=new_card()
        if a==1:
            a=int(input('congrats you got "A" now choose you want to have 1 or 11: '))
        if b==1 and card_sum(computer_cards)+11<=21:
            print("the computer has got 'A' and he chooses 11")
            b=11
        elif b==1 and card_sum(computer_cards)+11>21:
            print("the computer has got 'A' and he chooses 1")
            b=1
            
            
        your_cards.append(a)
        computer_cards.append(b)
        print(your_cards,'\n',computer_cards)
        if card_sum(your_cards)>21:
            break
        hit=input('type y to get another card and n to pass: ')
        
    p=cards[random.randint(0,12)]
    computer_cards.append(z)
    print(f'your score is: {card_sum(your_cards)}')
    print(f'computer score is: {card_sum(computer_cards)}')
    
    #result calculate
    if ((card_sum(computer_cards)<card_sum(your_cards) and ((card_sum(your_cards)<=21) or card_sum(computer_cards)>21))):
        print('You Win!')
    elif card_sum(your_cards)>21 and card_sum(computer_cards)>21:
        print('You lose!')
    elif card_sum(your_cards)<=21 and card_sum(computer_cards)>21:
        print('You Win!')
    else:
        print('You Lose!')
