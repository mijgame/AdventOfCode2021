from Helper import read_input

input = read_input('inputs/day4.txt')


# input = [
#     '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
#     '',
#     '22 13 17 11  0',
#     '8  2 23  4 24',
#     '21  9 14 16  7',
#     '6 10  3 18  5',
#     '1 12 20 15 19',
#     '',
#     '3 15  0  2 22',
#     '9 18 13 17  5',
#     '19  8  7 25 23',
#     '20 11 10 24  4',
#     '14 21 16 12  6',
#     '',
#     '14 21 17 24  4',
#     '10 16 15  9 19',
#     '18  8 23 26 20',
#     '22 11 13  6  5',
#     '2  0 12  3  7',
# ]


def parse_boards(input):
    boards = []
    board_states = []
    counter = 0
    board = []
    for line in filter(None, input[1:]):
        board.append([int(x) for x in filter(None, line.split(' '))])
        counter += 1

        if counter == 5:
            boards.append(board)
            state = []
            for i in range(0, 5):
                state.append([False] * 5)
            board_states.append(state)
            board = []
            counter = 0

    return boards, board_states


def play_round(number, boards, states):
    # Mark numbers
    for board in range(0, len(boards)):
        for y in range(0, 5):
            for x in range(0, 5):
                if boards[board][y][x] == number:
                    states[board][y][x] = True

    # Check for winners
    winning_indices = set()
    for board in range(0, len(boards)):
        for y in range(0, 5):
            if all(states[board][y]):
                winning_indices.add(board)
                break
        for x in range(0, 5):
            column = [row[x] for row in states[board]]
            if all(column):
                winning_indices.add(board)
                break

    return list(winning_indices)


def calculate_final_score(number, board, state):
    sum = 0
    for y in range(0, 5):
        for x in range(0, 5):
            if not state[y][x]:
                sum += board[y][x]
    return sum * number


boards, states = parse_boards(input)
called_numbers = [int(x.strip()) for x in input[0].split(',')]
last_score = -1
for number in called_numbers:
    winning_indices = play_round(number, boards, states)

    for index in sorted(winning_indices, reverse=True):
        last_score = calculate_final_score(number, boards[index], states[index])
        del boards[index]
        del states[index]
print(last_score)
