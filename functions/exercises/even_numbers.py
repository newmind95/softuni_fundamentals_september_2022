numbers_as_str = input().split()
numbers_list = list(map(int, filter(lambda x: int(x) % 2 == 0, numbers_as_str)))
print(numbers_list)
