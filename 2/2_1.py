sample_input = ['forward 5', 'down 5', 'forward 8', 'up 3',
                'down 8', 'forward 2']

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

h_pos = 0
depth = 0

for full_command in in_data:

    command, cmd_value = full_command.split(' ')

    if command == 'forward':
        h_pos += int(cmd_value)
    elif command == 'down':
        depth += int(cmd_value)
    elif command == 'up':
        depth -= int(cmd_value)

print(h_pos)
print(depth)
print(h_pos * depth)
