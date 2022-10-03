import re


def sorting_racers(racers: dict):
    return dict(sorted(racers.items(), key=lambda x: -x[1])[:3])


list_of_participants = input().split(', ')
pattern_for_names = r'[A-Za-z]+'
pattern_for_digits = r'[\d]+'

storing_racers = {}
command = input()
while not command == 'end of race':

    name_of_racer = ''
    distance_of_racer = ''
    calculate_distance = 0

    extracted_names_from_command = re.findall(pattern_for_names, command)
    for match in extracted_names_from_command:
        name_of_racer += match

    extracted_digits_from_command = re.findall(pattern_for_digits, command)
    for match in extracted_digits_from_command:
        distance_of_racer += match

    for digit in list(distance_of_racer):
        calculate_distance += int(digit)

    if name_of_racer in list_of_participants:
        if name_of_racer not in storing_racers:
            storing_racers[name_of_racer] = calculate_distance
        else:
            storing_racers[name_of_racer] += calculate_distance

    command = input()

for position, name_of_racer in enumerate(sorting_racers(storing_racers)):
    position += 1
    place = ''
    if position == 1:
        place = 'st place'
    if position == 2:
        place = 'nd place'
    if position == 3:
        place = 'rd place'
    print(f'{position}{place}: {name_of_racer}')
