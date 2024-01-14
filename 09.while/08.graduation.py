name=input()
grades_counter=0
average_grade=0
fail=0
while True:

    grade=float(input())
    if grade>=4:

        average_grade+=grade
        grades_counter+=1
    else:
        fail+=1
        if fail>1:
            grades_counter+=1
            print(f"{name} has been excluded at {grades_counter} grade")
            break
    if  grades_counter==12:
        average_grade=average_grade/grades_counter
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
