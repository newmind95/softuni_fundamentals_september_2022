sequence_of_targets = [int(x) for x in input().split()]
count_shooted_targets = 0
command = input()

while not command == 'End':

    targets_indices = int(command)

    if 0 <= targets_indices < len(sequence_of_targets):
        current_target = sequence_of_targets[targets_indices]

        for target_index in range(len(sequence_of_targets)):
            if sequence_of_targets[target_index] != -1:
                if sequence_of_targets[target_index] > current_target:
                    sequence_of_targets[target_index] -= current_target
                else:
                    sequence_of_targets[target_index] += current_target

        sequence_of_targets[targets_indices] = -1
        count_shooted_targets += 1

    command = input()

print(f'Shot targets: {count_shooted_targets} ->', end=' ')
print(f'{" ".join([str(x) for x in sequence_of_targets])}')
