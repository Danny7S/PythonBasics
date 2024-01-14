degrees=int(input())
time_of_day=input()
top=''
botton=''
if time_of_day=='Morning':
    if 10<=degrees<=18:
        top='Sweatshirt'
        botton='Sneakers'
    elif 18< degrees<=24:
        top = 'Shirt'
        botton = 'Moccasins'
    elif degrees>=25:
        top = 'T-Shirt'
        botton = 'Sandals'
if time_of_day=='Afternoon':
    if 10<=degrees<=18:
        top = 'Shirt'
        botton = 'Moccasins'
    elif 18< degrees<=24:
        top = 'T-Shirt'
        botton = 'Sandals'
    elif degrees>=25:
        top = 'Swim Suit'
        botton = 'Barefoot'
if time_of_day=='Evening':
    if 10<=degrees<=18:
        top = 'Shirt'
        botton = 'Moccasins'
    elif 18< degrees<=24:
        top = 'Shirt'
        botton = 'Moccasins'
    elif degrees>=25:
        top = 'Shirt'
        botton = 'Moccasins'
print(f"It's {degrees} degrees, get your {top} and {botton}.")