def sum_numbers(first: int, second: int) -> int:
    return first + second


def subtract(sum_num: int, third: int) -> int:
    return sum_num - third


def add_and_subtract(first: int, second: int, third: int) -> int:
    sum_number = sum_numbers(first, second)
    sub = subtract(sum_number, third)
    return sub


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
