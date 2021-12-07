from itertools import accumulate

sample_input = "16,1,2,0,4,2,7,1,2,14"

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

# start_positions = [int(x) for x in sample_input.split(',')]
start_positions = [int(x) for x in in_data[0].split(',')]

max_value = max(start_positions)
min_value = min(start_positions)

triangle_numbers = list(accumulate(range(min_value, max_value + 1)))

best_fuel = list()

for destination in range(min_value, max_value + 1):

    fuel_counter = 0

    for crab_sub in start_positions:

        fuel_distance = abs(crab_sub - destination)
        fuel_cost = triangle_numbers[fuel_distance]
        fuel_counter += fuel_cost

    best_fuel.append(fuel_counter)

print([(index, fuel_target) for index, fuel_target in enumerate(best_fuel) if fuel_target == min(best_fuel)])
