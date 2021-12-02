with open('input.txt') as in_file:
    in_data = [int(x.strip()) for x in in_file.readlines()]

a_point = 0
increase_counter = 0

for b_point in range(1, len(in_data)):
    if in_data[b_point] > in_data[a_point]:
        increase_counter += 1

    a_point = b_point

print(increase_counter)
