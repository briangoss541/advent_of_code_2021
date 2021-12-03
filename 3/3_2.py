from collections import defaultdict

sample_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
                '10000', '11001', '00010', '01010']

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]


def rating_finder(rating='oxygen'):

    target_list = in_data

    if rating == 'oxygen':
        preferred_bit = 1
        other_bit = 0
    elif rating == 'co2':
        preferred_bit = 0
        other_bit = 1

    for target_position in range(0, len(target_list[0])):

        round_dict = defaultdict(list)

        for number in target_list:
            for position, value in enumerate(number):
                round_dict[position].append(int(value))

        for position, values_list in round_dict.items():

            if position == target_position:
                if sum(values_list) / len(values_list) >= 0.5:
                    bit_flag = preferred_bit
                else:
                    bit_flag = other_bit

        target_list = [x for x in target_list if x[target_position] == str(bit_flag)]

        if len(target_list) == 1:
            print(target_list)
            return target_list[0]


oxygen_value = rating_finder(rating='oxygen')
co2_value = rating_finder(rating='co2')

print(oxygen_value)
print(co2_value)

oxygen_dec = int(oxygen_value, 2)
co2_dec = int(co2_value, 2)

print(oxygen_dec * co2_dec)
