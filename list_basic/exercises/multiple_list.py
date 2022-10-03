factor = int(input())
length_of_count = int(input())
result = []

for number in range(1, length_of_count + 1):
    result.append(number * factor)

print(result)
