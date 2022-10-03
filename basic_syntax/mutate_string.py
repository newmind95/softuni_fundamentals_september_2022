first_string = input()
second_string = input()
last_string = first_string
for character_index in range(len(first_string)):
    left_part_of_second_string = second_string[:character_index + 1]
    right_part_of_first_string = first_string[character_index + 1:]
    final_string = left_part_of_second_string + right_part_of_first_string
    if final_string == last_string:
        continue
    print(final_string)
    last_string = final_string
