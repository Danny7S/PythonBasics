import math

days=int(input())
first_km=float(input())
tot=first_km
for _ in range(days):
    percent=int(input())
    first_km=first_km+first_km*percent/100
    tot=tot+first_km
if tot>=1000:
    diff=tot-1000
    diff=math.ceil(diff)
    print(f"You've done a great job running {diff} more kilometers!")
else:
    diff=1000-tot
    diff=math.ceil(diff)
    print(f'Sorry Mrs. Ivanova, you need to run {diff} more kilometers')
