# # COFFEE MACHINE:
# Program Requirement:
# 1) report
# 2) check the amount of resources
# 3) Process coins
# 4) refund money if not enough.
# 5) send warning to the owner if resources not enough


import os
drink=input('Welcome to the machine\nEnter "on" to start the machine:')
    
resources={
    'water':1000,
    'milk':1000,
    'coffee':1000,
    'money':1000
}
drinks={
    'espresso':{
        'water':50,
        'coffee':18,
        'milk':0,
        'amount':1.50
    },
    'cappuccino':{
        'water':250,
        'milk':100,
        'coffee':24,
        'amount':3.00
    },
    'latte':{
        'water':200,
        'milk':150,
        'coffee':24,
        'amount':2.50
    }
}


def checkresources(drink):
    if drink=='espresso':
        if drinks['espresso']['water']<=resources['water'] and drinks['espresso']['coffee']<=resources['coffee']:
            return 1
        else:
            return -1
    
    if drink=='latte':
        if drinks['latte']['water']<=resources['water'] and drinks['latte']['coffee']<=resources['coffee'] and drinks['latte']['milk']<=resources['milk']:
            return 1
        else:
            return -1
    
    if drink=='cappuccino':
        
        if drinks['cappuccino']['water']<=resources['water'] and drinks['cappuccino']['coffee']<=resources['coffee'] and drinks['cappuccino']['milk']<=resources['milk']:
            return 1
        else:
            return -1
    else:
        return -1

    
    

# def addresources():
#     pass

def checkmoney(money,drink):
    total=money[0]*0.01+money[1]*0.05+money[2]*0.10+money[3]*0.25
    print('total= ',total)
    if total<drinks[drink]['amount']:
        return -1
    elif total==drinks[drink]['amount']:
        return 1
    else:
        return 1
    pass

def makecoffee(drink,money):
    print('Your coffee is being prepared...')
    
    for i in resources:
        if i!='money':
            resources[i]=resources[i]-drinks[drink][i]
        else:
            resources[i]=resources[i]+drinks[drink]['amount']
    
    print('''
                 S    
                S   
                 S
             _________
             \       /   
              \     /
               \___/
            ''')
    print("Enjoy your coffee!")
    print(f"Please collect your change of {round((money[0]*0.01+money[1]*0.05+money[2]*0.10+money[3]*0.25)-drinks[drink]['amount'],3)}")
    print('______________________________________________________\n\n\n')
    pass

# def updateinventory(money,drink):
#     pass

def report():
    print(f'Resources are as follows:\nWater={resources["water"]}\nMilk={resources["milk"]}\nCoffee={resources["coffee"]}\nMoney={resources["money"]} ')
    pass

def ping_owner(drink):
    pass

def refund(money):
    print('Please collect your money!!')
    print(f'Penny={money[0]}\nNickel={money[1]}\nDime={money[2]}\nQuarter={money[3]}')
    print('Please visit again!')
    pass

while drink!='off':
    drink=input('What would You like?espresso/latte/cappuccino: ')

    if drink== 'off':
        break
    elif drink=='report':
        report()
        continue
        
    if drink!='off':
        if checkresources(drink)==-1:
            print('insufficient material for the coffee try another')
            ping_owner(drink)
            
            
            continue
    
    if drink=='espresso' or drink=='cappuccino' or drink=='latte':
        penny=int(input('enter the number of coins(penny): '))
        nickel=int(input('enter the number of coins(nickel): '))
        dime=int(input('enter the number of coins(dime): '))
        quarter=int(input('enter the number of coins(quarter): '))
        money=[penny,nickel,dime,quarter]
        if checkmoney(money,drink)==1:
            makecoffee(drink,money)
            
        else:
            print('Sorry thats not enough money! please try again')
            refund(money)
            print('money refunded')
            
   
