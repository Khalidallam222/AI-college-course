def available_mov(puzzle: list):
    zero_index = puzzle.index(0)
    possible_moves = []
    # if empty in the first row
    if zero_index in [0, 1, 2]:
        possible_moves.append('v')
    # if empty in the second row
    if zero_index in [3, 4, 5]:
        possible_moves.append('v')
        possible_moves.append('^')
    # if empty in the third row
    if zero_index in [6, 7, 8]:
        possible_moves.append('^')

    # if empty in the first col
    if zero_index in [0, 3, 6]:
        possible_moves.append('>')
    # if empty in the second col
    if zero_index in [1, 4, 7]:
        possible_moves.append('>')
        possible_moves.append('<')
    # if empty in the third col
    if zero_index in [2, 5, 8]:
        possible_moves.append('<')

    return possible_moves


def apply_action(puzzle: list, selected_move):
    zero_index = puzzle.index(0)
    new_puzzle = puzzle[:]
    if selected_move == 'v':
        new_puzzle[zero_index], new_puzzle[zero_index + 3] = new_puzzle[zero_index + 3], new_puzzle[zero_index]
    if selected_move == '^':
        new_puzzle[zero_index], new_puzzle[zero_index - 3] = new_puzzle[zero_index - 3], new_puzzle[zero_index]
    if selected_move == '>':
        new_puzzle[zero_index], new_puzzle[zero_index + 1] = new_puzzle[zero_index + 1], new_puzzle[zero_index]
    if selected_move == '<':
        new_puzzle[zero_index], new_puzzle[zero_index - 1] = new_puzzle[zero_index - 1], new_puzzle[zero_index]

    return new_puzzle


def is_solved(puzzle):
    return puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]
