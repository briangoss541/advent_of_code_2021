from collections import deque
from statistics import median

sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

character_pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

character_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# in_data = sample_input.split('\n')


def line_reader(input_line):

    char_queue = deque()

    for index, char in enumerate(input_line):

        if char in character_pairs.keys():  # Opener
            char_queue.appendleft(character_pairs[char])
        elif char != char_queue[0]:  # Corrupt closer
            return 0
        elif char == char_queue[0]:  # Closer
            char_queue.popleft()

    closing_sum = 0
    for closing_char in char_queue:
        closing_sum *= 5
        closing_sum += character_points[closing_char]

    return closing_sum


points_list = list()
for line in in_data:
    print(line)
    line_result = line_reader(line)
    if line_result > 0:
        points_list.append(line_result)

print(points_list)
print(median(points_list))
