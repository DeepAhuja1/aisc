import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def main():
    print("=== Experiment 22: Winner-Take-All (Competitive) Learning Rule ===\n")

    m = int(input("Dimension of input vectors (features): "))
    num_clusters = int(input("Number of competitive cluster neurons: "))

    print("\nEnter initial weight vectors for each competitive neuron:")
    weights = []
    for j in range(num_clusters):
        row = [float(x) for x in input(f"Neuron {j+1} weights ({m} space-separated values): ").strip().split()]
        weights.append(row)

    n_samples = int(input("\nNumber of training samples: "))
    print(f"Enter {n_samples} training vectors:")
    samples = []
    for i in range(n_samples):
        row = [float(x) for x in input(f"Sample {i+1} ({m} space-separated values): ").strip().split()]
        samples.append(row)

    alpha = float(input("\nEnter learning rate (e.g., 0.1 to 0.5): "))
    epochs = int(input("Enter number of epochs: "))

    for epoch in range(epochs):
        for x in samples:
            # 1. Find winner neuron with minimum Euclidean distance
            distances = [euclidean_distance(x, weights[j]) for j in range(num_clusters)]
            winner = distances.index(min(distances))

            # 2. Update ONLY the winner's weights
            for d in range(m):
                weights[winner][d] += alpha * (x[d] - weights[winner][d])

    print("\n" + "=" * 45)
    print("Training Complete. Final Cluster Center Weights:")
    for j in range(num_clusters):
        formatted = ", ".join(f"{w:.4f}" for w in weights[j])
        print(f"Neuron {j+1}: [{formatted}]")
    print("=" * 45)

if __name__ == "__main__":
    main()