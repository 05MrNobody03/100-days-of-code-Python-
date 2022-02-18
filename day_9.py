'''
# Silent Bid Auction

import os
print(':Welcome to Bid Auction:')
conti='yes'
dict={}
while conti=='yes':
    name=input('name of the bidder: ')
    bid=int(input('Enter the bid ammount in $: '))
    dict[name]=bid
    conti=input('are there any other bidders: ')
    os.system('cls')
highest_bid=0
bid_by=''
for i in dict.keys():
    if dict[i]>highest_bid:
        highest_bid=dict[i]
        bid_by=i

    
print(f'the highest bid is {highest_bid} and by {bid_by}')
#grading problem

student_scores= {
    'harry':81,
    'ron': 78,
    'hermione': 99,
    'draco':74,
    'neville':62
}


for i in student_scores:
    if int(student_scores[i])>90:
        student_scores[i]='Outstanding'
    elif int(student_scores[i])>80 and int(student_scores[i])<=90:
        student_scores[i]='Exceeds Expectation'
    elif int(student_scores[i])>70 and int(student_scores[i])<=80:
        student_scores[i]='Average'
    elif int(student_scores[i])<=70:
        student_scores[i]='Fail'
        
print(student_scores)

'''
#nesting dictionary: 
travel_log={
    'France': ['paris','lille','dijon'],
    'germany': ['berlin','hamburg','stuttgart']
}

for i in travel_log:
    travel_log[i]={'cities_visited':travel_log[i]}

print(travel_log)

#nesting a dictionary in a list:

travel_log=[
    {'France': ['paris','lille','dijon']},
    {'germany': ['berlin','hamburg','stuttgart']}
    ]
print(travel_log)
