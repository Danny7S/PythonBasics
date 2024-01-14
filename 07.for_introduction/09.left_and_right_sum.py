n=int(input())
sum_l=0
sum_r=0
for combo in range(2*n):
    num= int(input())
    if combo<=n-1:
        sum_l+=num
    else:
        sum_r+=num
diff=sum_l-sum_r
if diff==0:
    print(f'Yes, sum = {sum_l}')
else:
    diff=abs(diff)
    print(f'No, diff = {diff}')