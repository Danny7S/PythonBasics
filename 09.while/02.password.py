num_dancer=int(input())
points=float(input())
season=input()
place=input()
money=points*num_dancer
dan_m=0
chari=0
if place=='Bulgaria':
    if season=='summer':
        money=money*0.95
    else:
        money=money*0.92
else:
    money = money + money * 0.5
    if season=='summer':
        money=money*0.9
    else:
        money=money*0.85
chari=money*0.75
dan_m=money*0.25/num_dancer
print(f'Charity - {chari:.2f}')
print(f'Money per dancer - {dan_m:.2f}')