sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# in_data = [x.strip() for x in sample_input.split('\n')]

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

instructions_dict = dict()
max_value = {'x': 0,
             'y': 0}

for index, direction in enumerate(in_data):

    direction_list = direction.split(' -> ')

    start_x, start_y = direction_list[0].split(',')
    end_x, end_y = direction_list[1].split(',')
    instructions_dict[index] = {'start_x': int(start_x),
                                'start_y': int(start_y),
                                'end_x': int(end_x),
                                'end_y': int(end_y)}

    for x_value in [start_x, end_x]:
        if int(x_value) > max_value['x']:
            max_value['x'] = int(x_value)
    for y_value in [start_y, end_y]:
        if int(y_value) > max_value['y']:
            max_value['y'] = int(y_value)

sea_map = [[0 for y in range(0, max_value['y'] + 1)] for x in range(0, max_value['x'] + 1)]

# Parse directions
for instruction_num, instruction_values in instructions_dict.items():
    print(instruction_values)

    if instruction_values['start_x'] - instruction_values['end_x'] == 0:

        # Direction
        if instruction_values['start_y'] < instruction_values['end_y']:
            range_step = 1
        else:
            range_step = -1

        for y_spot in range(instruction_values['start_y'], instruction_values['end_y'] + range_step, range_step):
            sea_map[instruction_values['start_x']][y_spot] += 1

    elif instruction_values['start_y'] - instruction_values['end_y'] == 0:

        # Direction
        if instruction_values['start_x'] < instruction_values['end_x']:
            range_step = 1
        else:
            range_step = -1

        for x_spot in range(instruction_values['start_x'], instruction_values['end_x'] + range_step, range_step):
            sea_map[x_spot][instruction_values['start_y']] += 1

    else:
        print("Can't parse")

overlap_count = 0
for row in sea_map:
    for spot in row:
        if spot >= 2:
            overlap_count += 1

print(overlap_count)
