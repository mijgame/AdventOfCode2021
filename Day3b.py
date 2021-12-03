from Helper import read_input

input = read_input('inputs/day3.txt')


def filter_by_bit(input, n, callback):
    ones = []
    zeros = []
    for entry in input:
        if entry[n] == '0':
            zeros.append(entry)
        else:
            ones.append(entry)
    return callback(zeros, ones)


oxygen_candidates = input.copy()
scrubber_candidates = input.copy()

# Oxygen
oxygen_value = None
scrubber_value = None
for bit in range(len(input[0])):
    oxygen_candidates = filter_by_bit(oxygen_candidates, bit,
                                      lambda zeros, ones: zeros if len(zeros) > len(ones) else ones)
    scrubber_candidates = filter_by_bit(scrubber_candidates, bit,
                                        lambda zeros, ones: zeros if len(zeros) <= len(ones) else ones)

    if len(oxygen_candidates) == 1:
        oxygen_value = int(oxygen_candidates[0], 2)
    if len(scrubber_candidates) == 1:
        scrubber_value = int(scrubber_candidates[0], 2)

print(oxygen_value * scrubber_value)
