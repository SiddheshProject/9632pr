def is_valid(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 3 or c_left > 3 or m_right > 3 or c_right > 3:
        return False
    if (c_left > m_left > 0) or (c_right > m_right > 0):
        return False
    return True

def next_states(state):
    m_left, c_left, b_pos, m_right, c_right = state
    if b_pos == 'left':
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        next_states = [(m_left-m, c_left-c, 'right', m_right+m, c_right+c) for m, c in moves]
    else:
        moves = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]
        next_states = [(m_left+m, c_left+c, 'left', m_right-m, c_right-c) for m, c in moves]
    return [state for state in next_states if is_valid(state)]

def dfs(start_state):
    frontier = []  
    frontier.append([start_state])
    explored = set()    
    while frontier:
        path = frontier.pop()
        current_state = path[-1]      
        if current_state == (0, 0, 'right', 3, 3):
            return path        
        for next_state in next_states(current_state):
            if next_state not in explored:
                new_path = path + [next_state]
                frontier.append(new_path)
                explored.add(next_state)
    return None
    
start_state = (3, 3, 'left', 0, 0)
path = dfs(start_state)

if path:
    for state in path:
        print(state)
else:
    print("No solution found.")

OUTPUT-:

test@lenovo6:~/Desktop$ python3 9632.py
(3, 3, 'left', 0, 0)
(3, 2, 'right', 0, 1)
(3, 1, 'left', 0, 2)
(1, 1, 'right', 2, 2)
(0, 1, 'left', 3, 2)
(0, 0, 'right', 3, 3)
test@lenovo6:~/Desktop$ 
