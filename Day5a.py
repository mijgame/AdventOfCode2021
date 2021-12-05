from Helper import read_input

input = read_input('inputs/day5.txt')


def parse_line(line):
    coords = line.split(' -> ')
    p1 = [int(x) for x in coords[0].split(',')]
    p2 = [int(x) for x in coords[1].split(',')]
    return p1, p2


positions = {}


def increment_pos(key: tuple):
    if key not in positions:
        positions[key] = 1
    else:
        positions[key] += 1


for input_line in input:
    line = parse_line(input_line)

    if line[0][0] == line[1][0]:
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        for i in range(start, end + 1):
            increment_pos((line[0][0], i))
    elif line[0][1] == line[1][1]:
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])
        for i in range(start, end + 1):
            increment_pos((i, line[0][1]))

count = 0
for value in positions.values():
    if value >= 2:
        count += 1

print(count)
