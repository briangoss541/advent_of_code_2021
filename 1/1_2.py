with open('input.txt') as in_file:
    in_data = [int(x.strip()) for x in in_file.readlines()]

a_point = 0
increase_counter = 0

for b_point in range(1, len(in_data)):

    if b_point + 3 > len(in_data):
        continue
    else:
        b_sum = sum(in_data[b_point:b_point + 3])

    a_sum = sum(in_data[a_point:a_point + 3])

    if b_sum > a_sum:
        increase_counter += 1

    a_point = b_point

print(increase_counter)
