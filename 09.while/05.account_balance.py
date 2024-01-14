chislo=int(input())
first=chislo%10
second=int((chislo/10)%10)
third=int((chislo/100)%10)
umn=0
for num in range(1,first+1):
    for num_d in range(1, second+1):
        for num_g in range(1, third+1):
            umn=num*num_d*num_g
            print(f'{num} * {num_d} * {num_g} = {umn};')