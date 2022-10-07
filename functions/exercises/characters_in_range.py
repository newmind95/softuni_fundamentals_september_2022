from typing import List


def range_of_symbols(char1: str, char2: str) -> List[str]:
    char1_ord = ord(char1)
    char2_ord = ord(char2)
    symbols_list = []

    for char_range in range(char1_ord + 1, char2_ord):
        as_char = chr(char_range)
        symbols_list.append(as_char)

    return symbols_list


starting_char, ending_char = input(), input()
result = range_of_symbols(starting_char, ending_char)
print(' '.join(result))
