from collections import deque

sample_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

# in_data = sample_input.split('\n')

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

octo_list = [[int(x) for x in y] for y in in_data]

flash_counter = 0

for step_num in range(1000):

    # for row in octo_list:
    #     print(row)
    #
    # print('\n')

    flash_queue = deque()
    flashed_coords = set()

    # Increase all energy levels
    round_list = octo_list.copy()

    for y, row in enumerate(octo_list):
        for x, cell_value in enumerate(row):
            round_list[y][x] = cell_value + 1
            if cell_value + 1 > 9:
                flash_queue.append((y, x))

    # Flashes!

    flash_masks = {(y, x) for y in [-1, 0, 1] for x in [-1, 0, 1]} - {0, 0}

    while len(flash_queue) > 0:

        flash_coord = flash_queue.popleft()

        if flash_coord in flashed_coords:
            round_list[flash_coord[0]][flash_coord[1]] = 0
            continue

        flash_counter += 1
        flashed_coords.add(flash_coord)
        round_list[flash_coord[0]][flash_coord[1]] = 0

        for y_mask, x_mask in flash_masks:
            new_y = flash_coord[0] + y_mask
            new_x = flash_coord[1] + x_mask
            if len(round_list) > new_y >= 0 and len(round_list[0]) > new_x >= 0:

                if (new_y, new_x) not in flashed_coords:
                    round_list[new_y][new_x] += 1
                    if round_list[new_y][new_x] > 9:
                        flash_queue.append((new_y, new_x))

    if len(flashed_coords) == len(round_list) * len(round_list[0]):
        print(f"All flashed at step {step_num + 1}")
        break

    octo_list = round_list
