try:
    fnumber = float(input('Enter the first value:'))
    snumber = float(input('Enter the second value:'))
    operator = input('What operator would you like to use?')

    if operator != '+' or '-' or '*' or '%':
        print('This operator is not supported by this calculator. Please try again.')
    if operator == '+':
        print(f'The results are:\n\tYour sum is:{fnumber + snumber}\n\tOperator of choice:{operator}\n\tFirst Value:{fnumber}\n\tSecond Value:{snumber}')
    elif operator == '-':
        print(f'The results are:\n\tYour sum is:{fnumber - snumber}\n\tOperator of choice:{operator}\n\tFirst Value:{fnumber}\n\tSecond Value:{snumber}')
    elif operator == '%':
        print(f'The results are:\n\tYour sum is:{fnumber % snumber}\n\tOperator of choice:{operator}\n\tFirst Value:{fnumber}\n\tSecond Value:{snumber}')
    elif operator == '*':
        print(f'The results are:\n\tYour sum is:{fnumber * snumber}\n\tOperator of choice:{operator}\n\tFirst Value:{fnumber}\n\tSecond Value:{snumber}')
    elif operator == '/':
                # if fnumber == 0 or snumber == 0:
                #     print('You cant divide by zero.')
                # else:
        print(f'The results are:\n\tYour sum is:{fnumber / snumber}\n\tOperator of choice:{operator}\n\tFirst Value:{fnumber}\n\tSecond Value:{snumber}')

except ZeroDivisionError as Z:
    print('Silly you, dont you know you cant divide by zero?')
    print(f'\tError details: {Z}')

except ValueError as G:
    print('What the heck man? I told you several times! ONLY NUMBERS!')
    print(f'\tError details: {G}')

