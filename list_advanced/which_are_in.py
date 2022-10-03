seq_of_strings1 = input().split(', ')
seq_of_strings2 = input()
result_list = []

for every_string in seq_of_strings1:
    if every_string in seq_of_strings2:
        result_list.append(every_string)

print(result_list)
