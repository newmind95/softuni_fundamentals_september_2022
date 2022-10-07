from typing import List


def check_palindrome(numbers: List[str]) -> List[str]:
    bool_list = []
    for number in numbers:
        if number == number[::-1]:
            bool_list.append('True')
        else:
            bool_list.append('False')

    return bool_list


numbers_list = input().split(', ')
result = check_palindrome(numbers_list)
print('\n'.join(result))

