command = input()
while not command == 'End':
    result = ''
    if command != 'SoftUni':
        for every_char in command:
            result += every_char * 2
        print(result)

    command = input()
