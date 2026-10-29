def main():
    print("=== Experiment 21: Center of Area (COA / Bisector) Defuzzification ===\n")

    n = int(input("Enter number of ordered points sampled across universe: "))
    
    z_vals = []
    mu_vals = []

    print("\nEnter universe points z (in strictly increasing order) and membership mu(z):")
    for i in range(n):
        z_vals.append(float(input(f"Point z[{i+1}]: ")))
        mu_vals.append(float(input(f"Membership mu[{i+1}]: ")))

    # Compute trapezoidal segment areas between consecutive points
    areas = []
    for i in range(n - 1):
        dz = z_vals[i+1] - z_vals[i]
        seg_area = 0.5 * (mu_vals[i] + mu_vals[i+1]) * dz
        areas.append(seg_area)

    total_area = sum(areas)
    half_area = total_area / 2.0

    if total_area == 0:
        print("\nError: Total area is zero.")
        return

    cum_area = 0.0
    bisector_z = z_vals[0]

    for i in range(len(areas)):
        if cum_area + areas[i] >= half_area:
            needed_area = half_area - cum_area
            dz = z_vals[i+1] - z_vals[i]
            # Interpolate within this segment
            fraction = needed_area / areas[i] if areas[i] > 0 else 0.0
            bisector_z = z_vals[i] + fraction * dz
            break
        cum_area += areas[i]

    print("\n" + "=" * 45)
    print(f"Total Area Under Curve : {total_area:.4f}")
    print(f"Half-Area Target       : {half_area:.4f}")
    print(f"Center of Area (z*)    : {bisector_z:.4f}")
    print("=" * 45)

if __name__ == "__main__":
    main()