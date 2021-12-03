from Helper import read_input

input = read_input('inputs/day3.txt')

zeros = [0] * len(input[0])
ones = [0] * len(input[0])

for column in range(len(input[0])):
    for entry in input:
        if entry[column] == '0':
            zeros[column] += 1
        else:
            ones[column] += 1

gamma = 0
epsilon = 0
for column in range(len(input[0])):
    if ones[column] > zeros[column]:
        gamma = (gamma << 1) | 1
        epsilon = epsilon << 1
    else:
        gamma = gamma << 1
        epsilon = (epsilon << 1) | 1

print(gamma * epsilon)

