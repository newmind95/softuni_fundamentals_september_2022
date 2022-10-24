sequence_of_integers = [int(num) for num in input().split()]
total_removed_elements = 0

while len(sequence_of_integers) != 0:
    index = int(input())

    element = 0

    if 0 <= index < len(sequence_of_integers):
    
        element = sequence_of_integers.pop(index)
        
    # If the given index is less than 0, remove the first element
    # of the sequence, and copy the last element to its place.
    elif index < 0:
        element = sequence_of_integers.pop[0]
        last_element = sequence_of_integers[-1]
        sequence_of_integers[0] = sequence_of_integers[-1]

    # If the given index is greater than the last index of the
    # sequence, remove the last element from the sequence,
    # and copy the first element to its place.
    else:
        element = sequence_of_integers[-1]
        sequence_of_integers[-1] = sequence_of_integers[0]

    for every_index in range(len(sequence_of_integers)):
        # Increase the value of all elements in the sequence
        # which are less or equal to the removed element
        # with the value of the removed element.
        if sequence_of_integers[every_index] <= element:
            sequence_of_integers[every_index] += element

        # Decrease the value of all elements in the sequence which
        # are greater than the removed element with the value
        # of the removed element.
        else:
            sequence_of_integers[every_index] -= element

    total_removed_elements += element

print(total_removed_elements)
