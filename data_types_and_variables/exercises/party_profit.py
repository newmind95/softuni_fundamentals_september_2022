from math import floor

group_size = int(input())
days_of_adventure = int(input())
counter_coins = 0

for every_day in range(1, days_of_adventure + 1):

    if every_day % 15 == 0:
        group_size += 5

    if every_day % 10 == 0:
        group_size -= 2

    if every_day % 3 == 0:
        counter_coins -= group_size * 3

    if every_day % 5 == 0:
        counter_coins += group_size * 20
        if every_day % 3 == 0:
            counter_coins -= group_size * 2

    counter_coins += 50
    counter_coins -= group_size * 2

coins_per_each_companion = floor(counter_coins / group_size)
print(f'{group_size} companions received', end=' ')
print(f'{coins_per_each_companion} coins each.')
