from collections import deque

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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# in_data = sample_input.split('\n')


def line_reader(input_line):

    char_queue = deque()

    for index, char in enumerate(input_line):

        if char in character_pairs.keys():  # Opener
            char_queue.appendleft(character_pairs[char])
        elif char != char_queue[0]:
            print(f'Corruption! at index {index} character {char}')
            return character_points[char]
        elif char == char_queue[0]:
            char_queue.popleft()

    return 0


points_list = list()
for line in in_data:
    print(line)
    points_list.append(line_reader(line))

print(sum(points_list))
