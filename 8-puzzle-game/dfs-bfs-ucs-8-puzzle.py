"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""
from functions import *
from puzzle8 import *

# ======================================================= # ================================================ # ========
def init_node(strategy, initial_state):
    initial_node = {'state': initial_state, 'path': []}
    if strategy == "UCS":
        initial_node['cost'] = 0
    return initial_node


def select_node(strategy, fringe):
    node = {}
    if strategy == 'DFS':
        node = fringe.pop()
    if strategy == 'BFS':
        node = fringe.pop(0)
    if strategy == 'UCS':
        fringe.sort(key=lambda x: x['cost'])
        node = fringe.pop(0)
    return node


def get_solution(strategy, node, visited):
    solution = {'path': node['path'], 'complexity': len(visited)}
    if strategy == 'UCS':
        solution['cost'] = node['cost']
    return solution


def get_cost(action, state):
    return 1


def add_node(strategy, current_node, action):
    next_state = apply_action(current_node['state'], action)
    next_node = {'state': next_state, 'path': current_node['path'] + [action]}
    if strategy == 'UCS':
        next_node['cost'] = current_node['cost'] + get_cost(action, current_node['state'])
    return next_node


def solve(strategy, initial_state):
    initial_node = init_node(strategy, initial_state)
    fringe = []
    visited = []
    fringe.append(initial_node)
    while fringe:
        current_node = select_node(strategy, fringe)
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if is_solved(current_node['state']):
            solution = get_solution(strategy, current_node, visited)
            return solution
        possible_actions = available_mov(current_node['state'])
        for action in possible_actions:
            next_node = add_node(strategy, current_node, action)
            fringe.append(next_node)
    return None


if __name__ == '__main__':
    puzzle = [
        3, 1, 2,
        4, 0, 5,
        6, 7, 8
    ]
    import random

    population = range(9)  # A list with numbers from 0 to 8
    unique_random_puzzle = random.sample(population, 9)
    print(unique_random_puzzle)

    # human_play(puzzle)
    solution1 = solve('DFS', unique_random_puzzle)
    solution2 = solve('BFS', unique_random_puzzle)
    print(solution1)
    print(solution2)

    # for move in solution['path']:
    #     puzzle = apply_action(puzzle, move)
    #     print_puzzle(puzzle)
