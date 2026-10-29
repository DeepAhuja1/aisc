def dls(current, goal, depth_limit, current_depth, graph, path, visited_in_path):
    """
    Recursive Depth-Limited Search implementation.
    - current: Node being evaluated
    - goal: Target node
    - depth_limit: User-defined maximum cutoff depth
    - current_depth: Depth of the current node from start (root = 0)
    """
    path.append(current)
    visited_in_path.add(current)
    
    print(f"Depth {current_depth}: Visiting '{current}' | Current Path: {' -> '.join(path)}")

    # 1. Goal Check
    if current == goal:
        return True

    # 2. Cutoff Check
    if current_depth >= depth_limit:
        path.pop()
        visited_in_path.remove(current)
        return False

    # 3. Explore Neighbors (Recursive Branching)
    for neighbor in graph.get(current, []):
        if neighbor not in visited_in_path:
            found = dls(neighbor, goal, depth_limit, current_depth + 1, graph, path, visited_in_path)
            if found:
                return True

    # Backtrack
    path.pop()
    visited_in_path.remove(current)
    return False


def main():
    print("=== Depth-Limited Search (DLS) - Experiment 9 ===\n")

    # Dynamic Graph Input
    is_directed = input("Is the graph directed? (y/n, default 'n'): ").strip().lower() == 'y'
    graph = {}

    print("\nEnter edges in format: [Node1] [Node2]")
    print("Type 'done' when you have finished entering edges.")
    
    while True:
        line = input("Edge (or 'done'): ").strip()
        if line.lower() == 'done':
            break
        parts = line.split()
        if len(parts) != 2:
            print("Invalid format. Please enter exactly two nodes (e.g., 'A B').")
            continue
        
        u, v = parts[0], parts[1]
        graph.setdefault(u, []).append(v)
        if not is_directed:
            graph.setdefault(v, []).append(u)
        else:
            graph.setdefault(v, [])

    if not graph:
        print("No graph entered. Exiting.")
        return

    print(f"\nAvailable nodes in graph: {list(graph.keys())}")
    start_node = input("Enter Start Node: ").strip()
    goal_node = input("Enter Goal Node: ").strip()

    if start_node not in graph or goal_node not in graph:
        print("Error: Start or Goal node not found in graph.")
        return

    depth_limit = int(input("Enter Depth Limit (Cutoff, where root is depth 0): "))

    path = []
    visited_in_path = set()

    print(f"\n--- Starting DLS from '{start_node}' to '{goal_node}' with Limit = {depth_limit} ---")
    found = dls(start_node, goal_node, depth_limit, 0, graph, path, visited_in_path)

    print("\n" + "=" * 45)
    if found:
        print("RESULT: GOAL FOUND WITHIN DEPTH LIMIT!")
        print(f"Path Taken: {' -> '.join(path)}")
        print(f"Depth Reached: {len(path) - 1}")
    else:
        print(f"RESULT: GOAL NOT FOUND WITHIN DEPTH LIMIT ({depth_limit}).")
        print("Cutoff occurred or no valid path exists.")
    print("=" * 45)


if __name__ == "__main__":
    main()