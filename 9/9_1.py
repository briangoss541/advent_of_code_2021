sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]


def low_pointer(input_map):

    low_points_list = list()
    risk_sum_list = list()

    coord_masks = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for y_coord, y_row in enumerate(input_map):
        for x_coord, cell_value in enumerate(y_row):

            adjacent_values = list()
            for y_mask, x_mask in coord_masks:
                if y_coord + y_mask >= 0 and x_coord + x_mask >= 0:
                    try:
                        adjacent_values.append(input_map[y_coord + y_mask][x_coord + x_mask])
                    except IndexError:
                        continue

            if cell_value < min(adjacent_values):
                low_points_list.append((y_coord, x_coord))
                risk_sum_list.append(1 + cell_value)

    print(f"Function sum is: {sum(risk_sum_list)}")

    return low_points_list


# height_map = [[int(y) for y in x] for x in sample_input.split('\n')]
height_map = [[int(y) for y in x] for x in in_data]

low_points = low_pointer(height_map)
