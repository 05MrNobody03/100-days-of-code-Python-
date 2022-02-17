str0='''
         ___________
        |           |
        |          
        |          
        |          
        |
-------------------------

'''
str1='''
         ___________
        |           |
        |           O
        |          
        |          
        |
-------------------------

'''
str2='''0
         ___________
        |           |
        |           O
        |           |
        |          
        |
-------------------------

'''

str3='''0
         ___________
        |           |
        |           O
        |          /|
        |          
        |
-------------------------

'''
str4='''0
         ___________
        |           |
        |           O
        |          /|\\
        |          
        |
-------------------------

'''
str5='''0
         ___________
        |           |
        |           O
        |          /|\\
        |          / 
        |
-------------------------

'''
str6='''0
         ___________
        |           |
        |           O
        |          /|\\
        |          / \\
        |
-------------------------

'''
import random
def check(hangman,char,word,last,life):
    if char in word:    
        while char in word:
            a=word.find(char)
            print(a)
            last[a]=char
            print(word)
            word=word.replace(char,'0',1)
            print(word)
    else:
        life-=1
        print(hangman[6-life])
    return word,last,life
        
hangman=[str0,str1,str2,str3,str4,str5,str6]
words=['hello','lucifer','eminem','cricket','ronaldo','christmax','summer','rainbow','programming','calculator']
life=6
word=words[random.randint(0,9)]
last=[]
for i in range(len(word)):
    last.append('_')
print(word,last)
while life!=0:
    print(''.join(last))
    char=input('Enter the character: ')
    word,last,life=check(hangman,char,word,last,life)
    if ''.join(last) == word:
        print('you won')
        break
if life==0:
    print('you lost')