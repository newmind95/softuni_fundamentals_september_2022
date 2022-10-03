for _ in range(int(input())):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif not (number == 88) and not (number == 86) and (number < 88):
        print('GREAT!')
    elif number > 88:
        print('Bye.')
