budget=float(input())
graphics_card_cout=int(input())
cpu_cout=int(input())
ram_count=int(input())
video_price=graphics_card_cout*250
cpu_price=video_price*0.35*cpu_cout
ram_price=video_price*0.1*ram_count
total=video_price+ram_price+cpu_price
if  graphics_card_cout>cpu_cout:
    total=total*0.85
if total>budget:
    needed_m=abs(total-budget)
    print(f"Not enough money! You need {needed_m:.2f} leva more!")
else:
    money_left=budget-total
    print(f"You have {money_left:.2f} leva left!")
