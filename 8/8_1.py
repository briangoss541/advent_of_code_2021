sample_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

# signal_patterns, output_values = sample_input.split(' | ')

render_lengths = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

counter = 0

for line in in_data:

    signal_patterns, output_values = line.split(' | ')

    signal_patterns = signal_patterns.split(' ')
    output_values = output_values.split(' ')

    for output_value in output_values:
        if len(output_value) in [2, 3, 4, 7]:
            counter += 1

print(counter)
# 482 too high