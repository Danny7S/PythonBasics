from sys import maxsize
min_num=maxsize
while True:
    data = input()
    if data !='Stop':
        num_o = int(data)
        if min_num>num_o:
            min_num=num_o
    else:
        break
print(min_num)