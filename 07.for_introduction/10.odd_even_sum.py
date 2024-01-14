n=int(input())
odd=0
even=0
for num in range(1, n+1):
    sss=int(input())
    if num%2==0:
        even+=sss
    else:
        odd+=sss
diff=even-odd
if diff==0:
    print('Yes')
    print(f'Sum = {even}')
else:
    diff=abs(diff)
    print('No')
    print(f'Diff = {diff}')
