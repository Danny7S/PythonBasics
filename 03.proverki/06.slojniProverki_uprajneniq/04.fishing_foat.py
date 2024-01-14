budget=int(input())
season=input()
numbers_of_fisherman=int(input())
price=0
discount=1
total=0
if season=='Summer' or season=='Autumn':
    price=4200
elif season=='Spring':
    price=3000
elif season=='Winter':
    price=2600
if numbers_of_fisherman<=6:
    discount=0.9
elif 6<numbers_of_fisherman<12:
    discount=0.85
else:
    discount=0.75
total=price*discount

if season!='Autumn' and numbers_of_fisherman%2==0:
    discount=0.95
    total=total*discount
diff= budget-total
if diff>=0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    diff=abs(diff)
    print(f"Not enough money! You need {diff:.2f} leva.")

# Ако групата е до 6 човека включително - отстъпка от 10%;
#
# · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
#
# · Ако групата е от 12 нагоре - отстъпка от 25%.