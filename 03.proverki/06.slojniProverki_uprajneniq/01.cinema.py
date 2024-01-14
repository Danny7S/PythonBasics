type_of_ticket=input()
rows=int(input())
coloms=int(input())
price=0
if type_of_ticket=='Premiere':
    price=coloms*rows*12
elif type_of_ticket=='Normal':
    price = coloms * rows * 7.5
elif type_of_ticket=='Discount':
    price = coloms * rows * 5
print(str(price) + ' leva')