number_of_groups=int(input())
musala=0
monban=0
kilimandjaro=0
k2=0
everest=0
tot=0
for _ in range(number_of_groups):
    group=int(input())
    tot+=group
    if group<=5:
        musala+=group
    if 6<= group <=12:
        monban+=group
    if 13<= group <=25:
        kilimandjaro+=group
    if 26<= group <=40:
        k2+=group
    if 41<= group:
        everest+=group

musala_percent=musala/tot*100
monban_percent=monban/tot*100
kilimandjaro_percent=kilimandjaro/tot*100
k2_percent=k2/tot*100
everest_percent=everest/tot*100
print(f'{musala_percent:.2f}%')
print(f'{monban_percent:.2f}%')
print(f'{kilimandjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')