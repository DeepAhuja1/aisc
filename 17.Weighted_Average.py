def main():
    print("=== Experiment 17: Weighted Average Defuzzification ===\n")

    n = int(input("Enter number of fuzzy sets / peak points: "))
    
    centroids = []
    weights = []

    print("\nEnter Centroid/Peak position (z) and corresponding Membership degree (mu(z)):")
    for i in range(n):
        z = float(input(f"Center z[{i+1}]: "))
        w = float(input(f"Membership mu(z[{i+1}]): "))
        centroids.append(z)
        weights.append(min(max(w, 0.0), 1.0))

    numerator = sum(centroids[i] * weights[i] for i in range(n))
    denominator = sum(weights)

    if denominator == 0:
        print("\nError: Sum of membership degrees cannot be zero.")
        return

    crisp_value = numerator / denominator

    print("\n" + "=" * 45)
    print(f"Sum(z * mu(z))  : {numerator:.4f}")
    print(f"Sum(mu(z))      : {denominator:.4f}")
    print(f"Defuzzified Crisp Value (z*): {crisp_value:.4f}")
    print("=" * 45)

if __name__ == "__main__":
    main()