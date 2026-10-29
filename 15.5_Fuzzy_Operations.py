def main():
    print("=== Experiment 15: Five Fuzzy Operations on Two Fuzzy Sets ===\n")

    elements = input("Enter universe elements (e.g., x1 x2 x3 x4): ").strip().split()
    n = len(elements)

    if n == 0:
        print("Universe of discourse cannot be empty.")
        return

    print("\n--- Enter Membership Values for Fuzzy Set A (0.0 to 1.0) ---")
    set_a = {}
    for el in elements:
        val = float(input(f"mu_A({el}): "))
        set_a[el] = min(max(val, 0.0), 1.0)

    print("\n--- Enter Membership Values for Fuzzy Set B (0.0 to 1.0) ---")
    set_b = {}
    for el in elements:
        val = float(input(f"mu_B({el}): "))
        set_b[el] = min(max(val, 0.0), 1.0)

    # 1. Union: mu_AUB(x) = max(mu_A(x), mu_B(x))
    fuzzy_union = {el: max(set_a[el], set_b[el]) for el in elements}

    # 2. Intersection: mu_AnB(x) = min(mu_A(x), mu_B(x))
    fuzzy_intersection = {el: min(set_a[el], set_b[el]) for el in elements}

    # 3. Complement: mu_A'(x) = 1 - mu_A(x)
    fuzzy_complement_a = {el: 1.0 - set_a[el] for el in elements}

    # 4. Algebraic Sum: mu_A+B(x) = mu_A(x) + mu_B(x) - (mu_A(x) * mu_B(x))
    fuzzy_alg_sum = {el: set_a[el] + set_b[el] - (set_a[el] * set_b[el]) for el in elements}

    # 5. Algebraic Product: mu_A.B(x) = mu_A(x) * mu_B(x)
    fuzzy_alg_product = {el: set_a[el] * set_b[el] for el in elements}

    # Display Results
    print("\n" + "=" * 55)
    print(f"{'Element':<10}{'Set A':<10}{'Set B':<10}{'Union':<10}{'Inters.':<10}{'Comp(A)':<10}{'AlgSum':<10}{'AlgProd':<10}")
    print("=" * 55)
    for el in elements:
        print(f"{el:<10}{set_a[el]:<10.2f}{set_b[el]:<10.2f}{fuzzy_union[el]:<10.2f}{fuzzy_intersection[el]:<10.2f}{fuzzy_complement_a[el]:<10.2f}{fuzzy_alg_sum[el]:<10.2f}{fuzzy_alg_product[el]:<10.2f}")
    print("=" * 55)

if __name__ == "__main__":
    main()