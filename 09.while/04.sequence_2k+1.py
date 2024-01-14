days=1
goal=8848
start=5364
while days<=5:
    if start>=goal:
        break
    night=input()
    if night=='END':
        break
    meters = int(input())
    if night=='Yes':
        days+=1
        if days>5:
            break

        start+=meters
    elif night=='No':
        start+=meters
if start<goal:
    print(f'Failed!')
    print(f'{start}')
else:
    print(f'Goal reached for {days} days!')