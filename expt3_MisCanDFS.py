class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c):
        self.left_m = left_m
        self.left_c = left_c
        self.boat = boat
        self.right_m = right_m
        self.right_c = right_c

    def __eq__(self, other):
        return (self.left_m, self.left_c, self.boat, self.right_m, self.right_c) == (
            other.left_m,
            other.left_c,
            other.boat,
            other.right_m,
            other.right_c,
        )

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))


def is_valid(state):
    if state.left_m < 0 or state.left_c < 0 or state.right_m < 0 or state.right_c < 0:
        return False
    if state.left_m > 3 or state.left_c > 3 or state.right_m > 3 or state.right_c > 3:
        return False
    if (state.left_c > state.left_m > 0) or (state.right_c > state.right_m > 0):
        return False
    return True


def dfs(current, visited, target):
    if current == target:
        return True

    visited.add(current)

    next_states = []

    if current.boat == "left":
        # Send 1 missionary
        next_states.append(State(current.left_m - 1, current.left_c, "right", current.right_m + 1, current.right_c))
        # Send 1 cannibal
        next_states.append(State(current.left_m, current.left_c - 1, "right", current.right_m, current.right_c + 1))
        # Send 1 missionary and 1 cannibal
        next_states.append(State(current.left_m - 1, current.left_c - 1, "right", current.right_m + 1, current.right_c + 1))
        # Send 2 missionaries
        next_states.append(State(current.left_m - 2, current.left_c, "right", current.right_m + 2, current.right_c))
        # Send 2 cannibals
        next_states.append(State(current.left_m, current.left_c - 2, "right", current.right_m, current.right_c + 2))
    else:
        # Bring 1 missionary back
        next_states.append(State(current.left_m + 1, current.left_c, "left", current.right_m - 1, current.right_c))
        # Bring 1 cannibal back
        next_states.append(State(current.left_m, current.left_c + 1, "left", current.right_m, current.right_c - 1))
        # Bring 1 missionary and 1 cannibal back
        next_states.append(State(current.left_m + 1, current.left_c + 1, "left", current.right_m - 1, current.right_c - 1))
        # Bring 2 missionaries back
        next_states.append(State(current.left_m + 2, current.left_c, "left", current.right_m - 2, current.right_c))
        # Bring 2 cannibals back
        next_states.append(State(current.left_m, current.left_c + 2, "left", current.right_m, current.right_c - 2))

    for next_state in next_states:
        if is_valid(next_state) and next_state not in visited:
            if dfs(next_state, visited, target):
                return True

    return False


def missionaries_cannibals_problem():
    left_m = int(input("Enter the number of missionaries on the left bank: "))
    left_c = int(input("Enter the number of cannibals on the left bank: "))
    boat = "left"
    right_m = 0
    right_c = 0
    initial_state = State(left_m, left_c, boat, right_m, right_c)

    right_m = int(input("Enter the number of missionaries on the right bank: "))
    right_c = int(input("Enter the number of cannibals on the right bank: "))
    boat = "right"
    target_state = State(0, 0, boat, right_m, right_c)

    visited = set()
    return dfs(initial_state, visited, target_state)


if __name__ == "__main__":
    if missionaries_cannibals_problem():
        print("Solution found.")
    else:
        print("No solution found.")
