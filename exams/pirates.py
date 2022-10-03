command = input()
dictionary = {}
while not command == 'Sail':

    tokens = command.split('||')
    cities = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])

    if cities in dictionary:
        dictionary[cities][0] += population
        dictionary[cities][1] += gold
    else:
        dictionary[cities] = [population, gold]

    command = input()

command = input()
while not command == 'End':

    if 'Plunder' in command:
        town = command.split('=>')[1]
        people = int(command.split('=>')[2])
        gold = int(command.split('=>')[3])
        dictionary[town][0] -= people
        dictionary[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if dictionary[town][0] == 0 or dictionary[town][1] == 0:
            dictionary.pop(town)
            print(f'{town} has been wiped off the map!')

    elif 'Prosper' in command:
        town = command.split('=>')[1]
        gold = int(command.split('=>')[2])
        if gold > 0:
            dictionary[town][1] += gold
            print(f'{gold} gold added to the city treasury.', end=' ')
            print(f'{town} now has {dictionary[town][1]} gold.')
        else:
            print('Gold added cannot be a negative number!')

    command = input()

if len(dictionary) > 0:
    print(f'Ahoy, Captain! There are {len(dictionary)} wealthy settlements to go to:')
    for town, people_gold in dictionary.items():
        print(f'{town} -> Population: {people_gold[0]} citizens, Gold: {people_gold[1]} kg')
else:
    print('Ahoy, Captain! All the targets have been plundered and destroyed!')
