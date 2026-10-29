import heapq

def a_star_search():
    print("=== A* Search Algorithm ===\n")
    
    is_directed = input("Is the graph directed? (y/n, default 'n'): ").strip().lower() == 'y'

    # 1. Get Graph Edges
    graph = {}
    print("\nEnter graph edges in the format: [Node1] [Node2] [Cost]")
    print("Type 'done' when finished.")
    
    while True:
        line = input("Edge (or 'done'): ").strip()
        if line.lower() == 'done':
            break
        parts = line.split()
        if len(parts) != 3:
            print("Invalid format. Use: Node1 Node2 Cost (e.g., A B 4.5)")
            continue
        try:
            u, v, cost = parts[0], parts[1], float(parts[2])
        except ValueError:
            print("Cost must be a valid number.")
            continue

        graph.setdefault(u, {})[v] = cost
        if not is_directed:
            graph.setdefault(v, {})[u] = cost
        else:
            graph.setdefault(v, {})

    if not graph:
        print("No graph entered. Exiting.")
        return

    # 2. Get Heuristics
    print("\n--- Heuristic Values h(n) ---")
    heuristics = {}
    for node in sorted(graph.keys()):
        while True:
            try:
                heuristics[node] = float(input(f"Heuristic h({node}): "))
                break
            except ValueError:
                print("Enter a valid numerical value.")

    # 3. Start and Goal
    print(f"\nAvailable nodes: {list(graph.keys())}")
    start_node = input("Enter Start Node: ").strip()
    goal_node = input("Enter Goal Node: ").strip()

    if start_node not in graph or goal_node not in graph:
        print("\nError: Start or Goal node not found in graph!")
        return

    # 4. A* Search Execution
    # Priority Queue stores tuples: (f_score, g_score, current_node, path)
    pq = [(heuristics[start_node], 0.0, start_node, [start_node])]
    g_scores = {node: float('inf') for node in graph}
    g_scores[start_node] = 0.0

    print("\n--- Executing A* Search ---")
    steps = 1

    while pq:
        f, g, current, path = heapq.heappop(pq)

        # Skip stale entries where a better path to current was already processed
        if g > g_scores[current]:
            continue

        print(f"\nStep {steps}: Expanding Node '{current}' | g={g:.2f}, h={heuristics[current]:.2f}, f={f:.2f}")
        steps += 1

        if current == goal_node:
            print("\n" + "=" * 45)
            print("GOAL REACHED!")
            print(f"Optimal Path : {' -> '.join(path)}")
            print(f"Total Cost   : {g:.2f}")
            print("=" * 45)
            return

        for neighbor, weight in graph.get(current, {}).items():
            tentative_g = g + weight
            if tentative_g < g_scores.get(neighbor, float('inf')):
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics.get(neighbor, 0.0)
                heapq.heappush(pq, (f_score, tentative_g, neighbor, path + [neighbor]))
                print(f"  -> Discovered/Updated '{neighbor}': g={tentative_g:.2f}, f={f_score:.2f}")

    print("\nGoal cannot be reached from the start node.")

if __name__ == "__main__":
    a_star_search()