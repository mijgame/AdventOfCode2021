from Helper import read_input
input = read_input('inputs/day1.txt', cast='int')

increases = 0
for i in range(1, len(input)):
    if input[i] > input[i - 1]:
        increases += 1
print(increases)

