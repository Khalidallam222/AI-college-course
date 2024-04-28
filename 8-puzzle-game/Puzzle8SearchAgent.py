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


class Puzzle8:
    def __init__(self, init_state):
        self.initial_state = init_state

    def get_initial_state(self):
        return self.initial_state

    def compute_heuristic(self, state):
        h = 0
        for i in range(9):
            if state[i] != i:
                h += 1
        return h

    def get_path(self, path):
        ret = []
        while type(path) is list and len(path):
            ret.insert(0, path[-1])
            path = path[0]
        return ret

    def get_cost(self, action, state):
        return 1

    def is_solved(self, puzzle):
        return puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def apply_action(self, puzzle: list, selected_move):
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

    def available_mov(self, puzzle: list):
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

    def print_puzzle(self, puzzle):
        p = ''
        for i in puzzle:
            if i == 0:
                p += ' '
            else:
                p += str(i)
        print(
            '-' * 13 + '\n' +
            '| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
            '-' * 13 + '\n' +
            '| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
            '-' * 13 + '\n' +
            '| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
            '-' * 13
        )


class DFS:
    def __init__(self):
        pass

    def init_node(self, problem):
        initial_node = {'state': problem.get_initial_state(), 'path': []}
        return initial_node

    def select_node(self, fringe):
        node = {}
        node = fringe.pop()
        return node

    def get_solution(self, problem, node, visited):
        solution = {'path': problem.get_path(node['path']), 'complexity': len(visited)}
        return solution

    def add_node(self, problem, current_node, action):
        next_state = problem.apply_action(current_node['state'], action)
        next_node = {'state': next_state, 'path': [current_node['path'], action]}
        return next_node


class BFS:
    def __init__(self):
        pass

    def init_node(self, problem):
        initial_node = {'state': problem.get_initial_state(), 'path': []}
        return initial_node

    def select_node(self, fringe):
        node = {}
        node = fringe.pop(0)
        return node

    def get_solution(self, problem, node, visited):
        solution = {'path': problem.get_path(node['path']), 'complexity': len(visited)}
        return solution

    def add_node(self, problem, current_node, action):
        next_state = problem.apply_action(current_node['state'], action)
        next_node = {'state': next_state, 'path': [current_node['path'], action]}
        return next_node


class UCS:
    def __init__(self):
        pass

    def init_node(self, problem):
        initial_node = {'state': problem.get_initial_state(), 'path': [], 'cost': 0}
        return initial_node

    def select_node(self, fringe):
        node = {}
        fringe.sort(key=lambda x: x['cost'])
        node = fringe.pop(0)
        return node

    def get_solution(self, problem, node, visited):
        solution = {'path': problem.get_path(node['path']), 'complexity': len(visited)}
        return solution

    def add_node(self, problem, current_node, action):
        next_state = problem.apply_action(current_node['state'], action)
        next_node = {'state': next_state, 'path': [current_node['path'], action],
                     'cost': current_node['cost'] + problem.get_cost(action, current_node['state'])}
        return next_node


class Greedy:
    def __init__(self):
        pass

    def init_node(self, problem):
        initial_node = {'state': problem.get_initial_state(), 'path': []}
        initial_node['heuristic'] = problem.compute_heuristic(initial_node["state"])
        return initial_node

    def select_node(self, fringe):
        node = {}
        fringe.sort(key=lambda x: x['heuristic'])
        node = fringe.pop(0)
        return node

    def get_solution(self, problem, node, visited):
        solution = {'path': problem.get_path(node['path']), 'complexity': len(visited)}
        return solution

    def add_node(self, problem, current_node, action):
        next_state = problem.apply_action(current_node['state'], action)
        next_node = {'state': next_state, 'path': [current_node['path'], action]}
        next_node["heuristic"] = problem.compute_heuristic(next_node["state"])
        return next_node


class Astar:
    def __init__(self):
        pass

    def init_node(self, problem):
        initial_node = {'state': problem.get_initial_state(), 'path': [], 'cost': 0}
        initial_node['f'] = initial_node['cost'] + problem.compute_heuristic(initial_node['state'])
        return initial_node

    def select_node(strategy, fringe):
        node = {}
        fringe.sort(key=lambda x: x['f'])
        node = fringe.pop(0)
        return node

    def get_solution(self, problem, node, visited):
        solution = {'path': problem.get_path(node['path']), 'complexity': len(visited)}
        return solution

    def add_node(self, problem, current_node, action):
        next_state = problem.apply_action(current_node['state'], action)
        next_node = {'state': next_state, 'path': [current_node['path'], action]}
        next_node['cost'] = backward_cost = current_node['cost'] + problem.get_cost(action, current_node['state'])
        next_node["f"] = problem.compute_heuristic(next_node["state"]) + backward_cost
        return next_node
    # ======================================================= # ================================================ #
    # ========


def solve(strategy, problem):
    initial_node = strategy.init_node(problem)
    fringe = []
    visited = []
    fringe.append(initial_node)
    while fringe:
        current_node = strategy.select_node(fringe)
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if problem.is_solved(current_node['state']):
            solution = strategy.get_solution(problem, current_node, visited)
            return solution
        possible_actions = problem.available_mov(current_node['state'])
        for action in possible_actions:
            next_node = strategy.add_node(problem, current_node, action)
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

    p = Puzzle8(unique_random_puzzle)
    s = Astar()
    # human_play(puzzle)
    # solution1 = solve('DFS', unique_random_puzzle)
    solution2 = solve(s, p)
    # print(solution1)
    print(solution2)

    puzzle = unique_random_puzzle
    for move in solution2['path']:
        puzzle = p.apply_action(puzzle, move)
        p.print_puzzle(puzzle)
