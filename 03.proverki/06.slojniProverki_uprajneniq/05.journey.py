budget=float(input())
season=input()
price=0
destination=''
place=''
if budget<=100:
    destination='Bulgaria'
    if season=='summer':
        place='Camp'
        price=budget*0.3
    else:
        place='Hotel'
        price = budget * 0.7
if 100< budget<=1000:
    destination='Balkans'
    if season=='summer':
        place='Camp'
        price=budget*0.4
    else:
        place='Hotel'
        price = budget * 0.8
if budget>1000:
    destination='Europe'
    place='Hotel'
    price=0.9*budget
print(f"Somewhere in {destination}")
print(f'{place} - {price:.2f}')