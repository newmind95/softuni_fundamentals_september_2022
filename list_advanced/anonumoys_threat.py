def read_input():
    return input().split()


def merge(lst: list, start_index: int, end_index: int):
    if start_index < 0:
        start_index = 0

    if end_index > len(lst) - 1:
        end_index = len(lst) - 1

    if start_index <= len(lst) <= end_index:
        for index in range(lst):
            lst[start_index] += lst[index]

    for iterate in range(end_index, start_index, -1):
        lst.pop(iterate)


sequence_of_strings = read_input()
