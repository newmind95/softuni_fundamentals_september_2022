from typing import List


def convert_str_to_int(numbers: List[str]) -> List[int]:
    new_list = []           # storing each number as integer
    for every_number in numbers:
        as_integer = int(every_number)
        new_list.append(as_integer)

    return new_list


def find_min_number(numbers: List[str], number: int) -> int:

    index_of_smallest = number   # index of smallest seen so far
    index = number + 1
    int_numbers = convert_str_to_int(numbers)
    while index != len(int_numbers):

        if int_numbers[index] < int_numbers[index_of_smallest]:
            index_of_smallest = index

        index += 1

    return index_of_smallest


def selection_sort(numbers: List[str]) -> List[int]:
    '''
    Reorder the list from smallest to largest.
    '''
    
    as_integer = convert_str_to_int(numbers)
    index = 0
    
    while index != len(as_integer):
        smallest_number = find_min_number(as_integer, index)
        as_integer[smallest_number], as_integer[index] = as_integer[index], as_integer[smallest_number]
        
        index += 1

    return as_integer


numbers_sequence = input().split()
result = selection_sort(numbers_sequence)
print(result)
