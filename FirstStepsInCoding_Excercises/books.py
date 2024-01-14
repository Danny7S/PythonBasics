from math import ceil
number_of_pages=int(input())
pages_per_hour=int(input())
days_left=int(input())
hours_per_day=number_of_pages//(pages_per_hour*days_left)
print(str(hours_per_day))