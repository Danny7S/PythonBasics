first_number=int(input())
second_number=int(input())
operation=input()
result=0
even=''
if operation=='+':
    result= first_number+second_number
elif operation=='-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/' and second_number!=0:
    result = first_number / second_number
elif operation == '%' and second_number!=0:
    result = first_number % second_number
if operation=='+' or operation=='-' or operation=='*':
    if result%2==1:
        even='odd'
    else:
        even='even'
    print(f"{first_number} {operation} {second_number} = {result} - {even}")
if operation=='/':
    if second_number==0:
        print(f"Cannot divide {first_number} by zero")
    else:
        print(f'{first_number} / {second_number} = {result:.2f}')
if operation=='%':
    if second_number==0:
        print(f"Cannot divide {first_number} by zero")
    else:
        print(f'{first_number} % {second_number} = {result}')
