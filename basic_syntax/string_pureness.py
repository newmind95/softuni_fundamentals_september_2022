for _ in range(int(input())):
    string = input()
    if not (',' in string) and not ('.' in string) and not ('_' in string):
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
