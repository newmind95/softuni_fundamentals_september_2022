text = input()
emoticons_list = []

for index in range(len(text)):
	if text[index] == ':':
		emoticons_list.append(text[index] + text[index + 1])

print('\n'.join(emoticons_list))
