from Helper import read_input

input = read_input('inputs/day4.txt')


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
    for board in range(0, len(boards)):
        for y in range(0, 5):
            if all(states[board][y]):
                return True, boards[board], states[board]
        for x in range(0, 5):
            column = [row[x] for row in states[board]]
            if all(column):
                return True, boards[board], states[board]
    return False, None, None


def calculate_final_score(number, board, state):
    sum = 0
    for y in range(0, 5):
        for x in range(0, 5):
            if not state[y][x]:
                sum += board[y][x]
    return sum * number


boards, states = parse_boards(input)
called_numbers = [int(x) for x in input[0].split(',')]
for number in called_numbers:
    has_winner, winning_board, winning_state = play_round(number, boards, states)
    if has_winner:
        score = calculate_final_score(number, winning_board, winning_state)
        print(score)
        break
