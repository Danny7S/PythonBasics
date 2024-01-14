import math

hour_of_exam=int(input())
minutes_of_exam=int(input())
hour_of_arival=int(input())
minutes_of_arival=int(input())

time_of_exam=hour_of_exam*60+minutes_of_exam
time_of_arival=hour_of_arival*60+minutes_of_arival
diff=time_of_exam-time_of_arival
minutes=0
hours=0
if 0<=diff<=30:
    print('On time')
    if diff!=0:
        print(f'{diff} minutes before the start')
if diff>30:
    print('Early')
    if diff<60:
        print(f'{diff} minutes before the start')
    else:
        hours=diff//60
        minutes=diff%60
        print(f'{hours:.0f}:{minutes:02d} hours before the start')
if diff<0:
    print('Late')
    diff=abs(diff)
    if diff>=60:
        hours=math.floor(diff/60)
        minutes=diff%60
        print(f'{hours:.0f}:{minutes:02d} hours after the start')
    else:
        minutes=diff
        print(f'{minutes} minutes after the start')




