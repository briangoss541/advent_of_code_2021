from collections import defaultdict

sample_input = '3,4,3,1,2'

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

initial_fishes = [int(x) for x in in_data[0].split(',')]

print(initial_fishes)

fish_ladder = defaultdict(int)

# Instantiate fish
for initial_timer in initial_fishes:
    fish_ladder[initial_timer] += 1

print(fish_ladder)

for day in range(1, 81):
    print(day)

    day_ladder = defaultdict(int)

    for timer_value, population_count in fish_ladder.items():

        if timer_value == 0:
            day_ladder[6] += population_count
            day_ladder[8] += population_count
        else:
            day_ladder[timer_value - 1] += population_count

    fish_ladder = day_ladder

print(fish_ladder)
print(sum([x for x in fish_ladder.values()]))
