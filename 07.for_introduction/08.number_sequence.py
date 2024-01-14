import sys
n=int(input())
min=-sys.maxsize
max=sys.maxsize
for _ in range(n):
    num=int(input())
    if num>min:
        min=num
    if num<max:
        max=num
print(f'Max number: {min}')
print(f'Min number: {max}')
