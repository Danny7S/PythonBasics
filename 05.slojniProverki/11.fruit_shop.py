product = input()
day_of_week = input()
quantity = float(input())
control = True
price=0
if day_of_week=='Saturday' or day_of_week=='Sunday':
    if product=='banana':
        price=2.7
    elif product=='apple':
        price=1.25
    elif product=='orange':
        price=0.9
    elif product=='grapefruit':
        price=1.6
    elif product=='kiwi':
        price=3
    elif product=='pineapple':
        price=5.6
    elif product=='grapes':
        price=4.2
    else:
        control=False
elif day_of_week=='Monday' or day_of_week=='Tuesday' or day_of_week=='Wednesday' or day_of_week=='Thursday' or day_of_week=='Friday':
    if product=='banana':
        price=2.5
    elif product=='apple':
        price=1.20
    elif product=='orange':
        price=0.85
    elif product=='grapefruit':
        price=1.45
    elif product=='kiwi':
        price=2.7
    elif product=='pineapple':
        price=5.5
    elif product=='grapes':
        price=3.85
    else:
        control=False
else:
    control=False
if control==False:
    print('error')
else:
    taksata=price*quantity
    print(f'{taksata:.2f}')


