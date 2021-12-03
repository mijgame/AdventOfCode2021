from Helper import read_input

input = read_input('inputs/day1.txt', cast='int')

increases = 0
old_window = input[0:3]
for i in range(4, len(input)+1):
    window = input[i - 3:i]
    if sum(window) > sum(old_window):
        increases += 1
    old_window = window
print(increases)
