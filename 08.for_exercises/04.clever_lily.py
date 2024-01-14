age_lilly=int(input())
price_wm=float(input())
price_toys=int(input())
savings=0
for n in range(1, age_lilly+1):
    if n%2==0:
        savings+=((n/2)*10)-1
    else:
        savings+=price_toys
diff=price_wm-savings
if diff<=0:
    diff=abs(diff)
    print(f"Yes! {diff:.2f}")
else:
    diff=abs(diff)
    print(f"No! {diff:.2f}")
