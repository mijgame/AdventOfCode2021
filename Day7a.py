from Helper import read_input

# input = [int(x) for x in read_input('inputs/day7.txt')[0].split(',')]
input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

min_pos = min(input)
max_pos = max(input)

best_pos = (-1, 9223372036854775807)
for pos in range(min_pos, max_pos + 1):
    fuel_sum = 0

    for crab in input:
        fuel_sum += abs(pos - crab)

    if fuel_sum < best_pos[1]:
        best_pos = (pos, fuel_sum)

print(best_pos[1])

