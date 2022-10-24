words = input().split()
word_even_length = [word for word in words if len(word) % 2 == 0]
print('\n'.join(word_even_length))
