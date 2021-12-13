from collections import defaultdict, deque

sample_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

# in_data = [x for x in sample_input.split('\n')]

with open('input.txt') as in_file:
    in_data = [x.strip() for x in in_file.readlines()]

# print(in_data)

nodes_set = set()
links_dict = defaultdict(set)

for instruction_data in in_data:
    start_node, end_node = instruction_data.split('-')
    nodes_set.add(start_node)
    nodes_set.add(end_node)
    links_dict[start_node].add(end_node)
    if start_node != 'start' and end_node != 'end':
        links_dict[end_node].add(start_node)

# print(nodes_set)
print(links_dict)

completed_list = list()

review_queue = deque()

review_queue.append(([], 'start'))

# print(review_queue)

while len(review_queue) > 0:

    target_data = review_queue.popleft()

    target_list = target_data[0]
    target_node = target_data[1]

    new_list = [x for x in target_list]
    new_list.append(target_node)

    if target_node == 'end':
        completed_list.append(new_list)
    else:
        for neighbor in links_dict[target_node]:
            if neighbor == neighbor.lower() and neighbor in target_list:
                continue
            else:
                review_queue.append((new_list, neighbor))

for path in completed_list:
    print(','.join(path))

print(len(completed_list))