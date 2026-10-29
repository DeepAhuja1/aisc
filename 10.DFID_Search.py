def print_board(state):
    """Prints the 3x3 puzzle board grid."""
    for i in range(0, 9, 3):
        print(f" {state[i]} | {state[i+1]} | {state[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def get_neighbors(state):
    """Generates valid next states by moving the blank tile (0)."""
    neighbors = []
    idx = state.index(0)
    row, col = divmod(idx, 3)
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

def is_solvable(start, goal):
    """Checks inversion parity to ensure the puzzle is mathematically solvable."""
    def count_inversions(s):
        arr = [x for x in s if x != 0]
        return sum(1 for i in range(len(arr)) for j in range(i + 1, len(arr)) if arr[i] > arr[j])
    return (count_inversions(start) % 2) == (count_inversions(goal) % 2)

def dls(current, goal, depth, path, path_set):
    """Depth-Limited Search helper with O(1) cycle detection."""
    path.append(current)
    path_set.add(current)

    if current == goal:
        return path

    if depth > 0:
        for neighbor in get_neighbors(current):
            if neighbor not in path_set:
                result = dls(neighbor, goal, depth - 1, path, path_set)
                if result is not None:
                    return result
                    
    path.pop()
    path_set.remove(current)
    return None

def iddfs(start, goal, max_depth):
    """Iterative Deepening Depth-First Search main loop."""
    for limit in range(max_depth + 1):
        print(f"-> Searching with depth limit: {limit}")
        path = []
        path_set = set()
        result = dls(start, goal, limit, path, path_set)
        if result is not None:
            print(f"\nGoal reached at depth limit {limit}!\n")
            return result
            
    print(f"\nGoal not found within max depth {max_depth}.")
    return None

def get_state_input(prompt):
    """Safely takes and validates 8-puzzle configuration input."""
    print(f"{prompt}\nEnter 9 numbers (0-8) separated by spaces (0 for blank tile):")
    while True:
        try:
            user_input = input("> ").strip().split()
            if len(user_input) != 9:
                print("Error: Please enter exactly 9 numbers.")
                continue
            state = tuple(int(x) for x in user_input)
            if set(state) != set(range(9)):
                print("Error: Numbers must be unique and range from 0 to 8.")
                continue
            return state
        except ValueError:
            print("Error: Please enter valid integers only.")

if __name__ == "__main__":
    print("--- 8-Puzzle Solver using DFID / IDDFS ---\n")
    start_state = get_state_input("--- Start State ---")
    goal_state = get_state_input("\n--- Goal State ---")
    
    if not is_solvable(start_state, goal_state):
        print("\nError: The given start state cannot reach the goal state (inversion parity mismatch).")
        exit()

    try:
        max_search_depth = int(input("\nEnter maximum search depth (recommended <= 10 for quick demo): ") or 10)
    except ValueError:
        max_search_depth = 10

    print("\nStarting configuration:")
    print_board(start_state)
    print("Target configuration:")
    print_board(goal_state)
    
    print("Starting IDDFS...\n")
    found_path = iddfs(start_state, goal_state, max_search_depth)

    if found_path:
        print(f"Solution found in {len(found_path) - 1} moves! Sequence:\n")
        for step, state in enumerate(found_path):
            print("Start:" if step == 0 else f"Move {step}:")
            print_board(state)