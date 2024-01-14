import math

series_name=input()
episode_duration=int(input())
break_duration=int(input())
time_left=break_duration*5/8
if time_left>=episode_duration:
    bonus=math.ceil(time_left-episode_duration)
    print(f"You have enough time to watch {series_name} and left with {bonus} minutes free time.")
else:
    needed_time=math.ceil(episode_duration-time_left)
    print(f"You don't have enough time to watch {series_name}, you need {needed_time} more minutes.")
