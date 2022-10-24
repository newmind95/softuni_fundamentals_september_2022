from typing import List


def find_wealthiest_part(populations: List[int]) -> int:
	'''
	Finds the wealthiest part of population and returns it
	'''

	wealthiest_seen_so_far = populations[0]
	for every_population_part in populations:
		if every_population_part > wealthiest_seen_so_far:
			wealthiest_seen_so_far = every_population_part
	return wealthiest_seen_so_far


number_of_population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())
wealthiest = find_wealthiest_part(number_of_population)
print(wealthiest)

# Loop trough population
for index, value in enumerate(number_of_population):
	pass



# Check if every part of the population has less than the wealthiest part
