number1, number2, number3 = [int(num) for num in input().split('.')]

if number3 <= 9:
    number3 += 1

    if number3 == 10:
        number3 = 0
        number2 += 1
    
    if number2 == 10:
        number2 = 0
        number1 += 1

print(f'{number1}.{number2}.{number3}')
