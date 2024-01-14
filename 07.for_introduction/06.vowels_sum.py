word=input()
a=0
e=0
i=0
o=0
u= 0
points=0
for letter in word:
    if letter=='a':
        points+=1
    if letter=='e':
        points+=2
    if letter=='i':
        points+=3
    if letter=='o':
        points+=4
    if letter=='u':
        points+=5
print(points)


