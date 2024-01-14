vacation_price = float(input())
puzzles = int(input())
speaking_doll = int(input())
fluffy_bear = int(input())
minion = int(input())
truck_toy = int(input())
sum_count = puzzles + fluffy_bear + speaking_doll + minion + truck_toy
sum_prize = puzzles * 2.6 + fluffy_bear * 4.1 + speaking_doll * 3 + minion * 8.2 + truck_toy * 2
if sum_count >= 50:
    sum_prize = sum_prize * 0.75
sum_prize = sum_prize * 0.9
money_left = sum_prize - vacation_price
if money_left >= 0:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = abs(money_left)
    print(f"Not enough money! {money_left:.2f} lv needed.")

