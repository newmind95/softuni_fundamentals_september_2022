WATER_TANK_CAPACITY_LITERS = 255
liters_in_tank = 0
number_of_lines = int(input())
for line in range(number_of_lines):
    liters_of_water = int(input())
    liters_in_tank += liters_of_water
    if liters_in_tank > WATER_TANK_CAPACITY_LITERS:
        liters_in_tank -= liters_of_water
        print('Insufficient capacity!')

print(liters_in_tank)
