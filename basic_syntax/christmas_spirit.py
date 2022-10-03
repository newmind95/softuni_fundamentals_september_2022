quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
total_cost = 0
total_spirit = 0

price_of_ornament_set, spirit_of_ornament_set = 2, 5
price_of_tree_skirt, spirit_of_tree_skirt = 5, 3
price_of_garland, spirit_of_garland = 3, 10
price_of_tree_lights, spirit_of_tree_lights = 15, 17

for day in range(1, days_left_until_christmas+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += price_of_ornament_set * quantity_of_decorations
        total_spirit += spirit_of_ornament_set
    if day % 3 == 0:
        total_cost += (price_of_tree_skirt + price_of_garland) \
                * quantity_of_decorations
    if day % 5 == 0:
        total_cost += price_of_tree_lights * quantity_of_decorations
        total_spirit += spirit_of_tree_lights
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += price_of_ornament_set + price_of_tree_skirt \
                                            + price_of_garland \
                                            + price_of_tree_lights

print(total_cost)
print(total_spirit)
