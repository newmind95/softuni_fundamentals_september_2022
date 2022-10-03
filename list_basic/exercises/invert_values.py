numbers_as_str = input().split()
result = []
for index in range(len(numbers_as_str)):
    current_number = int(numbers_as_str[index])
    result.append(current_number * -1)
print(result)
