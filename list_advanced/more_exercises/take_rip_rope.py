from typing import List


def find_numbers(text: str) -> List[int]:
    '''
    Finds numbers in the given string.
    '''

    result = []
    for char in text:
        if char.isdigit():
            number = int(char)
            result.append(number)

    return result


def find_non_numbers(text: str) -> List[str]:
    '''
    Finds non numbers in the given string.
    '''

    result = ''
    for char in text:
        if not char.isdigit():
            result += char

    return result


def get_even_numbers(numbers: List[int]) -> List[int]:
    '''
    Finds even index and store the corresponding value.
    Returns that list.
    '''

    even_numbers_list = []
    for index, value in enumerate(numbers):
        # Check if index is even.
        if index % 2 == 0:
            even_numbers_list.append(value)

    return even_numbers_list


def get_odd_numbers(numbers: List[int]) -> List[int]:
    '''
    Finds odd index and store the corresponding value.
    Returns that list.
    '''

    odd_numbers_list = []
    for index, value in enumerate(numbers):
        # Check if index is odd.		
        if index % 2 == 1:
            odd_numbers_list.append(value)

    return odd_numbers_list	


string = input()
numbers_list = find_numbers(string)
non_numbers_str = find_non_numbers(string)
even_numbers = get_even_numbers(numbers_list)
odd_numbers = get_odd_numbers(numbers_list)
final_string = ''
for index1, index2 in zip(even_numbers, odd_numbers):
    taken_string = non_numbers_str[:index1]
    non_numbers_str = non_numbers_str[index1:]
    non_numbers_str = non_numbers_str[index2:]
    final_string += taken_string 

print(final_string)
