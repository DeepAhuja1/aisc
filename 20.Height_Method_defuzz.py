def main():
    print("=== Experiment 20: Height Defuzzification Method ===\n")

    n = int(input("Enter number of fuzzy sets: "))

    centers = []
    heights = []

    for i in range(n):
        c = float(input(f"Enter center/peak position of Fuzzy Set {i+1} (c_{i+1}): "))
        h = float(input(f"Enter height (maximum membership) of Fuzzy Set {i+1} (h_{i+1}): "))
        centers.append(c)
        heights.append(min(max(h, 0.0), 1.0))

    num = sum(centers[i] * heights[i] for i in range(n))
    den = sum(heights)

    if den == 0:
        print("\nError: Total height cannot be zero.")
        return

    height_crisp = num / den

    print("\n" + "=" * 45)
    print(f"Sum(center * height) : {num:.4f}")
    print(f"Sum(height)          : {den:.4f}")
    print(f"Crisp Value (z*)     : {height_crisp:.4f}")
    print("=" * 45)

if __name__ == "__main__":
    main()