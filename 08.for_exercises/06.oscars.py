name_of_actor=input()
academy_points=float(input())
number_of_jury=int(input())
total_points=academy_points
oscar=1250.5
for _ in range(number_of_jury):
    name_of_jury=input()
    points_from_jury=float(input())
    total_points+=(len(name_of_jury)*points_from_jury)/2
    if oscar<=total_points:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
        break

if oscar-total_points>0:
    oscar-=total_points
    print(f"Sorry, {name_of_actor} you need {oscar:.1f} more!")
