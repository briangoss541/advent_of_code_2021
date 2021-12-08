from collections import defaultdict

sample_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

sample_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

render_lengths = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

final_segment_wiring = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

total_sum = 0


def decoder_ring(input_patterns):

    potential_wirings = {x: set('abcdefg') for x in list('abcdefg')}
    wiring_links = defaultdict(set)

    for signal_pattern in input_patterns:

        in_wire_set = {x for x in signal_pattern}

        if len(render_lengths[len(signal_pattern)]) == 1:

            target_digit = render_lengths[len(signal_pattern)][0]

            for out_wire in final_segment_wiring[target_digit]:
                potential_wirings[out_wire] = potential_wirings[out_wire] & in_wire_set

            wiring_links[target_digit] = ''.join(in_wire_set)

    digit_solutions = defaultdict(list)
    for signal_pattern in signal_patterns:

        in_wire_set = {x for x in signal_pattern}

        for potential_digit in render_lengths[len(signal_pattern)]:

            required_segments = {x for x in final_segment_wiring[potential_digit]}
            test_wiring_lists = [list(v) for k, v in potential_wirings.items() if k in required_segments]

            pools = [tuple(pool) for pool in test_wiring_lists]
            product_result = [[]]
            for pool in pools:
                product_result = [x + [y] for x in product_result for y in pool]

            for result in product_result:
                if set(result) == in_wire_set:
                    digit_solutions[potential_digit].append(signal_pattern)

    while True:
        for target_digit, solutions_list in digit_solutions.items():
            wiring_links_list = [''.join(x) for x in wiring_links.values()]
            if len(set(solutions_list) - set(wiring_links_list)) == 1:
                wiring_links[target_digit] = set(solutions_list) - set(wiring_links_list)

        if len(wiring_links) == 10:
            break

    wiring_links = {k: set(''.join(v)) for k, v in wiring_links.items()}

    return wiring_links


# for line in sample_input.split('\n'):
for line in in_data:

    signal_patterns, output_values = line.split(' | ')

    signal_patterns = signal_patterns.split(' ')
    output_values = output_values.split(' ')

    digit_mappings = decoder_ring(signal_patterns)

    output_number = list()
    for output_value in output_values:

        output_value_set = set(output_value)

        for digit in digit_mappings:
            if output_value_set == digit_mappings[digit]:
                output_number.append(str(digit))

    print(int(''.join(output_number)))

    total_sum += int(''.join(output_number))

print('\n', total_sum)
