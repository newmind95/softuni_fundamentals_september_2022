import re


destination_mapper = input()
places_on_the_map = ''
finded_destinations = []    # Store finded destinations
travel_points = 0
pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern, destination_mapper)
for match in matches:
    finded_destinations.append(match[1])
    travel_points += len(match[1])

result = ''
if matches:
    result += ", ".join(finded_destinations)
print('Destinations: ' + result)
print(f'Travel Points: {travel_points}')
