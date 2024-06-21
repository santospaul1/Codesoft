num1 = input('Enter the first number: ')
operator = input('Enter operator: ')
num2 = input('Enter the second number: ')

if operator == '+' :
    answer = int(num1) + int(num2)
elif operator == '-':
    answer = int(num1) - int(num2)
elif operator == '*':
    answer = int(num1) * int(num2)
elif operator == '/':
    answer = int(num1) / int(num2)
else:
    print('Operator not included')

print(answer)



