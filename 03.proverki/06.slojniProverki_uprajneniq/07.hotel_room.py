mount= input()
stay_lenght=int(input())
price_studio=0
price_apartament=0
if mount=='May' or mount=='October':
    price_studio=stay_lenght*50
    price_apartament=stay_lenght*65
    if 15>stay_lenght>7:
        price_studio=price_studio*0.95
    elif stay_lenght>14:
        price_studio=price_studio*0.7
elif mount == 'June' or mount == 'September':
    price_studio = stay_lenght * 75.2
    price_apartament = stay_lenght * 68.7
    if stay_lenght>14:
        price_studio=price_studio*0.8
elif mount== 'July' or mount=='August':
    price_studio = stay_lenght * 76
    price_apartament = stay_lenght * 77
if stay_lenght>14:
    price_apartament=price_apartament*0.9
print(f"Apartment: {price_apartament:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")