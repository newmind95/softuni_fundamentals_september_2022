recieve_age_of_kids = int(input())
consuming = 'drink '
if recieve_age_of_kids <= 14:
    consuming += 'toddy'
elif recieve_age_of_kids <= 18:
    consuming += 'coke'
elif recieve_age_of_kids <= 21:
    consuming += 'beer'
else:
    consuming += 'whisky'

print(consuming)
