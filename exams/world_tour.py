traveling_stops = input()
command = input()
while not command == 'Travel':

    if 'Add' in command:
        index = int(command.split(':')[1])
        string = command.split(':')[2]
        traveling_stops = traveling_stops[:index] + string + traveling_stops[index:]
        print(traveling_stops)

    elif 'Remove Stop' in command:
        start_index = int(command.split(':')[1])
        end_index = int(command.split(':')[2])
        if 0 <= start_index < len(traveling_stops) \
                and 0 <= end_index < len(traveling_stops):
            traveling_stops = traveling_stops[:start_index] + '' + traveling_stops[end_index+1:]
        print(traveling_stops)

    elif 'Switch' in command:
        old_string = command.split(':')[1]
        new_string = command.split(':')[2]
        traveling_stops = traveling_stops.replace(old_string, new_string)
        print(traveling_stops)

    command = input()


print(f'Ready for world tour! Planned stops: {traveling_stops}')
