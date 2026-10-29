def input_matrix(rows, cols, name):
    print(f"\nEnter membership values for relation {name} ({rows}x{cols}) row by row (space-separated between 0 and 1):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = [float(x) for x in input(f"Row {i + 1}: ").strip().split()]
                if len(row) != cols:
                    print(f"Error: Row must have exactly {cols} values.")
                    continue
                matrix.append([min(max(x, 0.0), 1.0) for x in row])
                break
            except ValueError:
                print("Error: Enter valid floating-point numbers.")
    return matrix

def print_matrix(mat, r_names, c_names):
    header = f"{'':<10}" + "".join(f"{c:<10}" for c in c_names)
    print(header)
    print("-" * len(header))
    for r_idx, row in enumerate(mat):
        row_str = f"{r_names[r_idx]:<10}" + "".join(f"{val:<10.2f}" for val in row)
        print(row_str)

def main():
    print("=== Experiment 16: Composition of Fuzzy Relations (Max-Min & Max-Product) ===\n")

    x_set = input("Enter elements of Universe X (e.g., x1 x2): ").strip().split()
    y_set = input("Enter elements of Universe Y (e.g., y1 y2 y3): ").strip().split()
    z_set = input("Enter elements of Universe Z (e.g., z1 z2): ").strip().split()

    p, q, r = len(x_set), len(y_set), len(z_set)

    # Relation R on (X x Y) and Relation S on (Y x Z)
    R = input_matrix(p, q, "R (X x Y)")
    S = input_matrix(q, r, "S (Y x Z)")

    # 1. Max-Min Composition: T(i, k) = max_j [ min(R(i, j), S(j, k)) ]
    max_min_comp = []
    for i in range(p):
        row = []
        for k in range(r):
            vals = [min(R[i][j], S[j][k]) for j in range(q)]
            row.append(max(vals))
        max_min_comp.append(row)

    # 2. Max-Product Composition: T(i, k) = max_j [ R(i, j) * S(j, k) ]
    max_prod_comp = []
    for i in range(p):
        row = []
        for k in range(r):
            vals = [R[i][j] * S[j][k] for j in range(q)]
            row.append(max(vals))
        max_prod_comp.append(row)

    print("\n" + "=" * 50)
    print("Max-Min Composition (R o S):")
    print_matrix(max_min_comp, x_set, z_set)

    print("\n" + "=" * 50)
    print("Max-Product Composition (R . S):")
    print_matrix(max_prod_comp, x_set, z_set)
    print("=" * 50)

if __name__ == "__main__":
    main()