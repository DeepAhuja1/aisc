import math

def minimax(depth, node_index, is_maximizing, scores, max_depth):
    # Base case: Leaf node reached
    if depth == max_depth:
        return scores[node_index], [node_index]

    if is_maximizing:
        left_score, left_path = minimax(depth + 1, node_index * 2, False, scores, max_depth)
        right_score, right_path = minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)

        # Maximize choice: take right child if strictly greater, else left
        if right_score > left_score:
            return right_score, [node_index] + right_path
        else:
            return left_score, [node_index] + left_path
    else:
        left_score, left_path = minimax(depth + 1, node_index * 2, True, scores, max_depth)
        right_score, right_path = minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)

        # Minimize choice: take right child if strictly smaller, else left
        if right_score < left_score:
            return right_score, [node_index] + right_path
        else:
            return left_score, [node_index] + left_path


def main():
    print("=== Minimax Search Algorithm (Experiment 13) ===\n")

    # Dynamic input options: by depth or by leaf array
    choice = input("Enter values by (1) Specifying tree depth or (2) Direct leaf list [1/2]: ").strip()

    if choice == '1':
        depth = int(input("Enter tree depth (e.g., 3 for 8 leaves, 4 for 16 leaves): "))
        num_leaves = 2 ** depth
        print(f"\nEnter {num_leaves} terminal leaf node values separated by spaces:")
        while True:
            try:
                raw = input("> ").strip().split()
                if len(raw) != num_leaves:
                    print(f"Error: Exactly {num_leaves} values required. You provided {len(raw)}.")
                    continue
                scores = [float(x) if '.' in x else int(x) for x in raw]
                break
            except ValueError:
                print("Error: Enter valid numbers only.")
    else:
        print("\nEnter all terminal leaf node scores separated by spaces (count must be a power of 2):")
        while True:
            try:
                raw = input("> ").strip().split()
                scores = [float(x) if '.' in x else int(x) for x in raw]
                n = len(scores)
                if n == 0 or (n & (n - 1)) != 0:
                    print(f"Error: Number of leaf nodes ({n}) is not a power of 2 (e.g., 2, 4, 8, 16, 32).")
                    continue
                break
            except ValueError:
                print("Error: Enter valid numbers only.")

    max_depth = int(math.log2(len(scores)))
    root_player = input("\nDoes MAX start at the root? (y/n, default 'y'): ").strip().lower() != 'n'

    best_score, best_path = minimax(0, 0, root_player, scores, max_depth)

    print("\n" + "=" * 45)
    print("GAME TREE EVALUATION COMPLETED")
    print(f"Total Leaves Evaluated : {len(scores)}")
    print(f"Tree Depth             : {max_depth}")
    print(f"Optimal Root Value     : {best_score}")
    print("=" * 45)

    print("\nOptimal Path Traversal:")
    for d, idx in enumerate(best_path):
        if d == max_depth:
            print(f"Depth {d} -> Leaf Index {idx} (Terminal Value = {scores[idx]})")
        else:
            current_player = "MAX" if (d % 2 == 0 if root_player else d % 2 != 0) else "MIN"
            print(f"Depth {d} -> {current_player} Decision Node Index {idx}")

    print("\nPath Index Sequence:", " -> ".join(map(str, best_path)))


if __name__ == "__main__":
    main()