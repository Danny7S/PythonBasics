from sys import maxsize
n=int(input())
max =-maxsize
sum = 0
diff=0
for _ in range(n):
    num = int(input())
    if max < num:
        max = num
    sum += num
diff= sum-2*max
if diff==0:

    print("Yes")
    print(f"Sum = {max}")
else:
    diff=abs(diff)
    print("No")
    print(f"Diff = {diff}")

