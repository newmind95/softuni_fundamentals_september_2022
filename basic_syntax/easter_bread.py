budget = float(input())
price_for_kg_flour = float(input())
counter_loaves = 0
counter_colored_eggs = 0

price_for_kg_eggs = price_for_kg_flour + (price_for_kg_flour * (75 / 100))
price_for_liter_milk = price_for_kg_flour + (price_for_kg_flour * (25 / 100))
number_of_loaf = price_for_kg_eggs + price_for_liter_milk * 0.250

while budget >= number_of_loaf:
    budget -= number_of_loaf
    counter_loaves += 1
    counter_colored_eggs += 3
    if counter_loaves % 3 == 0:
        counter_colored_eggs -= (counter_loaves - 2)

print(f'You made {counter_loaves} loaves of Easter bread!', end=' ')
print(f'Now you have {counter_colored_eggs} eggs and {budget:.2f}BGN left.')
