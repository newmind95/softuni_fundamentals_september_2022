started_char_index = int(input())
last_char_index = int(input())
for every_char_index in range(started_char_index, last_char_index + 1):
    print(chr(every_char_index), end=' ')
