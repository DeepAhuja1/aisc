def main():
    print("=== Experiment 19: Center of Sum (COS) Defuzzification ===\n")

    num_points = int(input("Enter number of discrete universe points (z): "))
    z_points = []
    for i in range(num_points):
        z_points.append(float(input(f"  Point z[{i+1}]: ")))

    num_sets = int(input("\nEnter number of overlapping fuzzy sets: "))
    
    # Store membership values for each set across all z points
    all_mu = []
    for k in range(num_sets):
        print(f"\nEnter membership degrees for Fuzzy Set {k+1}:")
        mu_k = []
        for i in range(num_points):
            val = float(input(f"  mu_{k+1}(z = {z_points[i]}): "))
            mu_k.append(min(max(val, 0.0), 1.0))
        all_mu.append(mu_k)

    # Sum of membership across all fuzzy sets for each point z_i
    sum_mu_per_point = [sum(all_mu[k][i] for k in range(num_sets)) for i in range(num_points)]

    numerator = sum(z_points[i] * sum_mu_per_point[i] for i in range(num_points))
    denominator = sum(sum_mu_per_point)

    if denominator == 0:
        print("\nError: Total sum of memberships is zero.")
        return

    cos_value = numerator / denominator

    print("\n" + "=" * 45)
    print(f"Numerator Sum(z_i * Sum(mu_k)) : {numerator:.4f}")
    print(f"Denominator Sum(Sum(mu_k))     : {denominator:.4f}")
    print(f"Center of Sum Crisp Value (z*) : {cos_value:.4f}")
    print("=" * 45)

if __name__ == "__main__":
    main()