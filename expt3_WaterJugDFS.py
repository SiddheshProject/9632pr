class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))


def dfs(current, visited, target, jug1_capacity, jug2_capacity):
    if current == target:
        return True

    visited.add(current)

    next_states = []

    # Fill jug1
    next_states.append(State(jug1_capacity, current.jug2))

    # Fill jug2
    next_states.append(State(current.jug1, jug2_capacity))

    # Empty jug1
    next_states.append(State(0, current.jug2))

    # Empty jug2
    next_states.append(State(current.jug1, 0))

    # Pour jug1 to jug2
    pour_amount = min(current.jug1, jug2_capacity - current.jug2)
    next_states.append(State(current.jug1 - pour_amount, current.jug2 + pour_amount))

    # Pour jug2 to jug1
    pour_amount = min(current.jug2, jug1_capacity - current.jug1)
    next_states.append(State(current.jug1 + pour_amount, current.jug2 - pour_amount))

    for next_state in next_states:
        if next_state not in visited:
            if dfs(next_state, visited, target, jug1_capacity, jug2_capacity):
                return True

    return False


def water_jug_problem():
    jug1_capacity = int(input("Enter the capacity of jug 1: "))
    jug2_capacity = int(input("Enter the capacity of jug 2: "))
    target_jug1 = int(input("Enter the desired amount of water in jug 1: "))
    target_jug2 = int(input("Enter the desired amount of water in jug 2: "))
    target = State(target_jug1, target_jug2)
    initial_state = State(0, 0)
    visited = set()
    return dfs(initial_state, visited, target, jug1_capacity, jug2_capacity)


if __name__ == "__main__":
    if water_jug_problem():
        print("Goal state is reachable.")
    else:
        print("Goal state is not reachable.")
