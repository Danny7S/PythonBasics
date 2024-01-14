from sys import maxsize
max_num = -maxsize
while True:
    data=input()
    if data=='Stop':
        break
    numbers=int(data)
    if numbers>max_num:
        max_num=numbers
print(max_num)