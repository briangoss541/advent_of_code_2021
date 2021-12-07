from statistics import median

sample_input = "16,1,2,0,4,2,7,1,2,14"

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

start_positions = [int(x) for x in in_data[0].split(',')]

destination = median(start_positions)

fuel_counter = 0

for crab_sub in start_positions:

    fuel_cost = abs(crab_sub - destination)
    fuel_counter += fuel_cost

print(destination)
print(fuel_counter)
