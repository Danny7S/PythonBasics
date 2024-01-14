movie_budget=float(input())
statists_number=int(input())
clothing_price=float(input())

decor=movie_budget*0.1
if statists_number>150:
    clothing_price=clothing_price*0.9

money=movie_budget-decor-clothing_price*statists_number
if  money>=0:
    print("Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")
else:
    print('Not enough money!')
    money=abs(money)
    print(f"Wingard needs {money:.2f} leva more.")