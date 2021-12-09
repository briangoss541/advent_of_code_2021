from tqdm import tqdm

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


def basin_finder(input_map):

    low_points_list = low_pointer(input_map)

    covered_coords = set()

    basin_list = list()

    # coord_shifts = {(y, x) for x in [-1, 0, 1] for y in [-1, 0, 1]} - {(0, 0)}
    coord_shifts = {(-1, 0), (0, -1), (1, 0), (0, 1)}

    for inital_low_point in tqdm(low_points_list):
        print(inital_low_point)

        if inital_low_point in covered_coords:
            continue

        target_points = [inital_low_point]

        basin_size = 0

        while len(target_points) > 0:

            target_point = target_points.pop()

            if target_point in covered_coords:
                continue

            covered_coords.add(target_point)

            basin_size += 1

            for coord_shift in coord_shifts:

                new_y = target_point[0] + coord_shift[0]
                new_x = target_point[1] + coord_shift[1]

                if new_y >= 0 and new_x >= 0:
                    try:
                        if input_map[new_y][new_x] != 9:
                            target_points.append((new_y, new_x))
                    except IndexError:
                        continue

        basin_list.append(basin_size)

    return basin_list


# height_map = [[int(y) for y in x] for x in sample_input.split('\n')]
height_map = [[int(y) for y in x] for x in in_data]

# low_points = low_pointer(height_map)
basin_data = basin_finder(height_map)

basin_sort = sorted(basin_data, reverse=True)
print(basin_sort[0] * basin_sort[1] * basin_sort[2])

# 83867200 too high
# 400000 too low
