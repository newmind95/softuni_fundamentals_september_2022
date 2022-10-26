from typing import List, Tuple

'''
A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what, and that is exactly what you are called to do for this problem.
On the first line, you will be given the population (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population. 
There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible". 

Input:
2, 3, 5, 15, 75
5

Output:
[5, 5, 5, 15, 70]

'''


def find_wealthiest_part(populations: List[int]) -> Tuple[int]:
	'''
	Finds the wealthiest part of the population and returns it.
	'''

	wealthiest_seen_so_far = populations[0]
	index_of_wealthiest = 0
	for index in range(len(populations)):
		if populations[index] > wealthiest_seen_so_far:
			wealthiest_seen_so_far = populations[index]
			index_of_wealthiest = index
	
	return wealthiest_seen_so_far, index_of_wealthiest


number_of_population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())


# Loop trough population
for index in range(len(number_of_population)):
	if number_of_population[index] < minimum_wealth:
		redisturbed_wealth = minimum_wealth - number_of_population[index]
		wealthiest, wealthiest_index = find_wealthiest_part(number_of_population)
		if wealthiest - redisturbed_wealth >= minimum_wealth:
			number_of_population[wealthiest_index] -= redisturbed_wealth
			number_of_population[index] += redisturbed_wealth
			

if sum(number_of_population) >= len(number_of_population) * minimum_wealth:
	print(number_of_population)
else:
	print('No equal distribution possible')
