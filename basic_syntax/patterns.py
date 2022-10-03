number = int(input())
for row in range(1, number + 1):
    for col in range(0, row):
        print('*', end='')
    print()

for row in range(number - 1, -1, -1):
    for col in range(row, 0, -1):
        print('*', end='')
    print()
