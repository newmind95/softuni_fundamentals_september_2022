from typing import Tuple


def odd_even_sum(digits: str) -> Tuple[int]:
    even_digits_sum = 0
    odd_digits_sum = 0

    for every_digit in digits:
        digit_as_int = int(every_digit)
        if digit_as_int % 2 == 0:
            even_digits_sum += digit_as_int
        else:
            odd_digits_sum += digit_as_int

    return even_digits_sum, odd_digits_sum


digits_as_str = input()
total_even_digits, total_odd_digits = odd_even_sum(digits_as_str)
print(f'Odd sum = {total_odd_digits}, Even sum = {total_even_digits}')
