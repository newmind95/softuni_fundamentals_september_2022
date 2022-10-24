number_of_rooms = int(input())
total_free_chairs = 0
game_on = True

for every_room in range(number_of_rooms):
    chairs, visitors = input().split()
    visitors = int(visitors)
    counter_chairs = chairs.count('X')

    if counter_chairs >= visitors:
        total_free_chairs += abs(counter_chairs - visitors) 

    else:
        needed_chairs_in_roomo = visitors - counter_chairs
        print(f'{needed_chairs_in_roomo} more chairs needed in room {every_room}')
        game_on = False

if game_on is True:
    print(f'Game On, {total_free_chairs} free chairs left.')
