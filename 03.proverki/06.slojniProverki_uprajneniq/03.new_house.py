type_of_flowers=input()
number_of_flowers=int(input())
budget=int(input())
price=0
total=0
discount=1
if type_of_flowers=="Roses":
    price=5
    if  number_of_flowers>80:
        discount=0.9
        total=price*discount*number_of_flowers
    else:
        total=price*discount*number_of_flowers


if type_of_flowers == "Dahlias":
    price = 3.8
    if number_of_flowers > 90:
        discount = 0.85
        total = price * discount * number_of_flowers
    else:
        total = price * discount * number_of_flowers

if type_of_flowers == "Tulips":
    price = 2.8
    if number_of_flowers > 80:
        discount = 0.85
        total = price * discount * number_of_flowers
    else:
        total = price * discount * number_of_flowers

if type_of_flowers == "Narcissus":
    price = 3
    if number_of_flowers < 120:
        discount = 1.15
        total = price * discount * number_of_flowers
    else:
        total = price * discount * number_of_flowers

if type_of_flowers == "Gladiolus":
    price = 2.5
    if number_of_flowers < 80:
        discount = 1.2
        total = price * discount * number_of_flowers
    else:
        total = price * discount * number_of_flowers
diff= budget-total
if diff>=0:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {diff:.2f} leva left.')
else:
    diff=abs(diff)
    print(f"Not enough money, you need {diff:.2f} leva more.")