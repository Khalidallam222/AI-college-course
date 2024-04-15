"""
Search(initil_state):
    initial_node = {initial_state, path}
    fringe = [initial_node]
    while fringe is not empty:
        select node form fringe according to a strategy
        if node in visited: continue
        if goal: return solution
        from state get possible actions
        from actions get next_states
        from next_states generate next_nodes (successors)
        fringe +=[next_nodes]
    return failure

"""


# DFS
def solve_dfs(initial_state):
    initial_node = {'state': initial_state, 'path': []}
    fringe = []
    visited = []
    fringe.append(initial_node)
    while fringe:
        current_node = fringe.pop()
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if is_goal(current_node['state']):
            return current_node['path']
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(action, current_node['state'])
            next_node = {'state': next_state, 'path': current_node['path'] + [action]}
            fringe.append(next_node)
    return None


# BFS
def solve_bfs(initial_state):
    initial_node = {'state': initial_state, 'path': []}
    fringe = []
    visited = []
    fringe.append(initial_node)
    while fringe:
        current_node = fringe.pop(0)
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if is_goal(current_node['state']):
            return current_node['path']
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(action, current_node['state'])
            next_node = {'state': next_state, 'path': current_node['path'] + [action]}
            fringe.append(next_node)
    return None


# UCS
def solve_ucs(initial_state):
    initial_node = {'state': initial_state, 'path': [], 'cost': 0}
    fringe = []
    visited = []
    fringe.append(initial_node)
    while fringe:
        fringe.sort(key=lambda x: x['cost'])
        current_node = fringe.pop(0)
        if current_node['state'] in visited:
            continue
        visited.append(current_node['state'])
        if is_goal(current_node['state']):
            solution = {'path': current_node['path'], 'complexity': len(visited), 'cost': current_node['cost']}
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_state = get_state(action, current_node['state'])
            next_node = {'state': next_state, 'path': current_node['path'] + [action],
                         'cost': current_node['cost'] + get_cost(action, current_node['state'])}
            fringe.append(next_node)
    return None


# =============================================================================================================================================================
# =============================================================================================================================================================
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

def add_node(strategy, current_node, action):
    next_state = get_state(action, current_node['state'])
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
        if is_goal(current_node['state']):
            solution = get_solution(strategy, current_node, visited)
            return solution
        possible_actions = get_actions(current_node['state'])
        for action in possible_actions:
            next_node = add_node(strategy, current_node, action)
            fringe.append(next_node)
    return None
