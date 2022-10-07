from typing import List


def convert_str_to_int(numbers: List[str]) -> List[int]:

    new_list = []
    for every_number in numbers:
        as_integer = int(every_number)
        new_list.append(as_integer)
    
    return new_list

def find_max_number(numbers: List[str]) -> int:

    as_integers = convert_str_to_int(numbers)
    max_num_seen_so_far = as_integers[0] 
    index = 0
    while index != len(as_integers):

        if as_integers[index] > max_num_seen_so_far:
            max_num_seen_so_far = as_integers[index]

        index += 1

    return max_num_seen_so_far


def find_min_number(numbers: List[str]) -> int:

    as_integers = convert_str_to_int(numbers)
    min_num_seen_so_far = as_integers[0] 
    index = 0
    while index != len(as_integers):

        if as_integers[index] < min_num_seen_so_far:
            min_num_seen_so_far = as_integers[index]

        index += 1

    return min_num_seen_so_far


def sum_numbers(numbers: List[str]) -> int:

    as_integers = convert_str_to_int(numbers)
    total = 0
    index = 0
    while index != len(as_integers):

        total += as_integers[index]

        index += 1

    return total


numbers_sequence = input().split()
max_number = find_max_number(numbers_sequence)
min_number = find_min_number(numbers_sequence)
total = sum_numbers(numbers_sequence)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is {total}')
