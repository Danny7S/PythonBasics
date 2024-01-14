days_of_stay=int(input())-1
type_of_room=input()
oppinion=input()
price=1
if type_of_room=='room for one person':
    price=18*days_of_stay
elif type_of_room=='apartment':
    price = 25 * days_of_stay
    if days_of_stay<10:
        price=price*0.7
    elif 10<=days_of_stay<=15:
        price=price*0.65
    else:
        price=price*0.5
elif type_of_room=='president apartment':
    price = 35 * days_of_stay
    if days_of_stay<10:
        price=price*0.9
    elif 10<=days_of_stay<=15:
        price=price*0.85
    else:
        price=price*0.8
if oppinion=='positive':
    price=1.25*price
else:
    price=0.9*price
print(f'{price:.2f}')