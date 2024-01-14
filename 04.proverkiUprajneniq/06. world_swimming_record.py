record_time=float(input())
distance_m=float(input())
time_s_m=float(input())

ivan_time=distance_m*time_s_m
delay=(distance_m//15)*12.5
ivan_time=ivan_time+delay
if  ivan_time>=record_time:
    time_d=abs(record_time-ivan_time)
    print(f"No, he failed! He was {time_d:.2f} seconds slower.")
else:
    time_u=record_time-ivan_time
    print(f" Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")