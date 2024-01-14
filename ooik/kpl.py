import math

dni=int(input())
ost_hr=int(input())
hr_pur=float(input())
hr_vt=float(input())
hr_tr=float(input())
izqd=(hr_tr+hr_pur+hr_vt)*dni
diff=abs(ost_hr-izqd)



if ost_hr>=izqd:
    diff=math.floor(diff)
    print(f'{diff} kilos of food left.')
else:
    diff=math.ceil(diff)
    print(f'{diff} more kilos of food are needed.')
