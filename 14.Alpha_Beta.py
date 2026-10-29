import math

pruned_count = 0

def alpha_beta_pruning(depth, node_index, is_maximizing, scores, max_depth, alpha, beta):
    global pruned_count

    # Base Case: Terminal Leaf Node
    if depth == max_depth:
        return scores[node_index], [node_index]

    if is_maximizing:
        max_eval = -math.inf
        best_path = []

        # Left child
        left_score, left_path = alpha_beta_pruning(
            depth + 1, node_index * 2, False, scores, max_depth, alpha, beta
        )
        if left_score > max_eval:
            max_eval = left_score
            best_path = [node_index] + left_path
        alpha = max(alpha, max_eval)

        # Beta cut-off condition: Prune right child
        if beta <= alpha:
            pruned_count += 1
            print(f"  [Pruning] Beta cutoff at MAX node {node_index} (depth {depth}): alpha={alpha} >= beta={beta}. Right child pruned.")
            return max_eval, best_path

        # Right child
        right_score, right_path = alpha_beta_pruning(
            depth + 1, node_index * 2 + 1, False, scores, max_depth, alpha, beta
        )
        if right_score > max_eval:
            max_eval = right_score
            best_path = [node_index] + right_path
        alpha = max(alpha, max_eval)

        return max_eval, best_path

    else:
        min_eval = math.inf
        best_path = []

        # Left child
        left_score, left_path = alpha_beta_pruning(
            depth + 1, node_index * 2, True, scores, max_depth, alpha, beta
        )
        if left_score < min_eval:
            min_eval = left_score
            best_path = [node_index] + left_path
        beta = min(beta, min_eval)

        # Alpha cut-off condition: Prune right child
        if beta <= alpha:
            pruned_count += 1
            print(f"  [Pruning] Alpha cutoff at MIN node {node_index} (depth {depth}): beta={beta} <= alpha={alpha}. Right child pruned.")
            return min_eval, best_path

        # Right child
        right_score, right_path = alpha_beta_pruning(
            depth + 1, node_index * 2 + 1, True, scores, max_depth, alpha, beta
        )
        if right_score < min_eval:
            min_eval = right_score
            best_path = [node_index] + right_path
        beta = min(beta, min_eval)

        return min_eval, best_path


def main():
    global pruned_count
    pruned_count = 0

    print("=== Alpha-Beta Pruning Algorithm (Experiment 14) ===\n")

    choice = input("Enter values by (1) Specifying tree depth or (2) Direct leaf list [1/2]: ").strip()

    if choice == '1':
        depth = int(input("Enter tree depth (e.g., 3 for 8 leaves, 4 for 16 leaves): "))
        num_leaves = 2 ** depth
        print(f"\nEnter {num_leaves} terminal leaf node scores separated by spaces:")
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
                    print(f"Error: Number of leaf nodes ({n}) is not a power of 2.")
                    continue
                break
            except ValueError:
                print("Error: Enter valid numbers only.")

    max_depth = int(math.log2(len(scores)))
    root_player = input("\nDoes MAX start at the root? (y/n, default 'y'): ").strip().lower() != 'n'

    print("\n--- Search Execution & Cut-offs ---")
    best_score, best_path = alpha_beta_pruning(
        0, 0, root_player, scores, max_depth, -math.inf, math.inf
    )

    print("\n" + "=" * 45)
    print("ALPHA-BETA PRUNING COMPLETED")
    print(f"Tree Depth             : {max_depth}")
    print(f"Total Leaves In Tree   : {len(scores)}")
    print(f"Cut-offs Triggered     : {pruned_count}")
    print(f"Optimal Value at Root  : {best_score}")
    print("=" * 45)

    print("\nOptimal Path Traversal:")
    for d, idx in enumerate(best_path):
        if d == max_depth:
            print(f"Depth {d} -> Leaf Index {idx} (Score = {scores[idx]})")
        else:
            player = "MAX" if (d % 2 == 0 if root_player else d % 2 != 0) else "MIN"
            print(f"Depth {d} -> {player} Node Index {idx}")

    print("\nPath Index Sequence:", " -> ".join(map(str, best_path)))


if __name__ == "__main__":
    main()