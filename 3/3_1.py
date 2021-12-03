from collections import defaultdict

sample_input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100',
                '10000', '11001', '00010', '01010']

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

bit_dict = defaultdict(list)

for number in in_data:
    for position, value in enumerate(number):
        bit_dict[position].append(int(value))

gamma_dict = dict()

for position, values_list in bit_dict.items():

    if sum(values_list) / len(values_list) > 0.5:
        gamma_dict[position] = 1
    else:
        gamma_dict[position] = 0

gamma_list = list()
epsilon_list = list()
for position in range(len(gamma_dict)):
    gamma_list.append(str(gamma_dict[position]))

    if gamma_dict[position] == 1:
        epsilon_list.append('0')
    elif gamma_dict[position] == 0:
        epsilon_list.append('1')

gamma_value = ''.join(gamma_list)
epsilon_value = ''.join(epsilon_list)

gamma_dec = int(gamma_value, 2)
epsilon_dec = int(epsilon_value, 2)

print(gamma_dec * epsilon_dec)
