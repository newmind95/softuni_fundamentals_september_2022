def find_smallest_number(first: int, second: int,
                         third: int) -> int:

    if first < second and first < third:
        return first

    elif second < first and second < third:
        return second

    elif third < first and third < second:
        return third


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = find_smallest_number(first_number, second_number,
                              third_number)
print(result)
