city=input()
sales=float(input())
control=True
commision=0
if  city=='Sofia':
    if 0 <=sales <= 500:
        commision=sales*0.05
    elif 500 < sales <= 1000:
        commision=sales*0.07
    elif 1000 < sales <= 10000:
        commision=sales*0.08
    elif sales > 10000:
        commision=sales*0.12
    else:
        control=False
elif city == 'Plovdiv':
    if 0 <=sales <= 500:
        commision=sales*0.055
    elif 500 < sales <= 1000:
        commision=sales*0.08
    elif 1000 < sales <= 10000:
        commision=sales*0.12
    elif sales > 10000:
        commision=sales*0.145
    else:
        control=False

elif city == 'Varna':
    if 0 <=sales <= 500:
        commision=sales*0.045
    elif 500 < sales <= 1000:
        commision=sales*0.075
    elif 1000 < sales <= 10000:
        commision=sales*0.1
    elif sales > 10000:
        commision=sales*0.13
    else:
        control=False
else:
    control=False
if  control==False:
    print('error')
else:
    print(f'{commision:.2f}')