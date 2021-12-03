from Helper import read_input_split_by
input = [x.split(' ') for x in read_input_split_by('inputs/day2.txt', '\n')]
input = [[x[0], int(x[1])] for x in input]

pos = 0
depth = 0
aim = 0

for entry in input:
    if entry[0] == 'forward':
        pos += entry[1]
        depth += aim * entry[1]
    elif entry[0] == 'down':
        aim += entry[1]
    elif entry[0] == 'up':
        aim -= entry[1]

print(pos * depth)