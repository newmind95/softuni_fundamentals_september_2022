sequence_of_strings = input().split()

command = input()
while not command == '3:1':

    tokens = command.split()
    type_of_command = tokens[0]
    
    if 'merge' == type_of_command:
        start_index = int(tokens[1])
        end_index = int(tokens[2])

        if start_index < 0:
            start_index = 0

        if end_index > len(sequence_of_strings) -1:
            end_index = len(sequence_of_strings) -1

        for index in range(len(sequence_of_strings)):
            if index in range(start_index +1, end_index +1):
                sequence_of_strings[start_index] += sequence_of_strings[index]

        for iterate in range(end_index, start_index, -1):
            sequence_of_strings.pop(iterate)

    if 'divide' == type_of_command:
        index = int(tokens[1])
        partitions = int(tokens[2])
        step = 0
        if partitions > len(sequence_of_strings[index]):
            step = 1
        else:
            step = len(sequence_of_strings[index]) // partitions
            
        divide_part = sequence_of_strings.pop(index)
        start = 0
        for partition in range(partitions):
            if partition == partitions - 1:
               strings_input = sequence_of_strings.insert(index, divide_part[start::])
               break
            else:
               sequence_of_strings.insert(index, divide_part[start: start + step:])
            start += step 
            index += 1
    command = input()


print(' '.join(sequence_of_strings))
