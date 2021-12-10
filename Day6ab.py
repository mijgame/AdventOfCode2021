from Helper import read_input

input = [int(x) for x in read_input('inputs/day6.txt')[0].split(',')]


def simulate_day(state):
    new_fish = state[0]
    for i in range(0, 8):
        state[i] = state[i + 1]
    state[6] += new_fish
    state[8] = new_fish


state = {}
for i in range(9):
    state[i] = 0
for age in input:
    state[age] += 1

for day in range(256):
    simulate_day(state)

sum = 0
for i in state:
    sum += state[i]

print(sum)
