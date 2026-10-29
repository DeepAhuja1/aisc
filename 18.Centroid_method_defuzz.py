def main():
    print("=== Experiment 18: Centroid Defuzzification Method ===\n")

    n = int(input("Enter number of sampled points across universe of discourse: "))
    
    z_vals = []
    mu_vals = []

    print("\nEnter pairs of (z, mu(z)) points:")
    for i in range(n):
        z = float(input(f"Universe point z[{i+1}]: "))
        mu = float(input(f"Membership value mu[{i+1}]: "))
        z_vals.append(z)
        mu_vals.append(min(max(mu, 0.0), 1.0))

    num = sum(z * mu for z, mu in zip(z_vals, mu_vals))
    den = sum(mu_vals)

    if den == 0:
        print("\nError: Total area under membership function is zero.")
        return

    centroid_z = num / den

    print("\n" + "=" * 45)
    print(f"Numerator Sum(z * mu(z)) : {num:.4f}")
    print(f"Denominator Sum(mu(z))   : {den:.4f}")
    print(f"Centroid Value (z*)      : {centroid_z:.4f}")
    print("=" * 45)

if __name__ == "__main__":
    main()