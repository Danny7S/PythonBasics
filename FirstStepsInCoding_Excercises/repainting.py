nylon=(int(input())+2)*1.5
paint=(int(input())*1.1)*14.50
razreditel=int(input())*5
hours=int(input())
materials=nylon+paint+razreditel+0.4
work=hours*materials*0.3
print(work+materials)

