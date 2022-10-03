number_of_lines = int(input())
total_sum_of_chars = 0
for every_line in range(number_of_lines):
    letter_per_line = input()
    total_sum_of_chars += ord(letter_per_line)
print(f'The sum equals: {total_sum_of_chars}')
