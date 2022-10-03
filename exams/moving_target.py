sequence_of_targets = [int(x) for x in input().split()]
command = input()

while not command == 'End':

    tokens = command.split()
    if 'Shoot' == tokens[0]:
        index, power = int(tokens[1]), int(tokens[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] -= power
        is_shot = sequence_of_targets[index] == 0
        if is_shot:
            sequence_of_targets.remove(0)

    if 'Add' == tokens[0]:
        index, value = int(tokens[1]), int(tokens[2])
        if 0 <= index < len(sequence_of_targets):
            sequence_of_targets[index] += value
            print(f'Add {value} at index: {index}')
        else:
            print('Invalid placement!')

    if 'Strike' == tokens[0]:
        index, radius = int(tokens[1]), int(tokens[2])
        strike_before_index = index - radius
        strike_after_index = index + radius
        if 0 <= strike_before_index < len(sequence_of_targets) \
                and 0 <= strike_after_index < len(sequence_of_targets):
            sequence_of_targets = sequence_of_targets[0:strike_before_index] \
                    + sequence_of_targets[strike_after_index+1::]
        else:
            print('Strike missed!')

    command = input()

print(sequence_of_targets)
