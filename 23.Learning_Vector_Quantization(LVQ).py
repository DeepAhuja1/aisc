import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def main():
    print("=== Experiment 23: Learning Vector Quantization (LVQ) Rule ===\n")

    m = int(input("Dimension of input vectors (features): "))
    num_proto = int(input("Number of prototype / codebook weight vectors: "))

    weights = []
    proto_classes = []

    print("\nEnter prototype weight vectors and their assigned classes:")
    for j in range(num_proto):
        row = [float(x) for x in input(f"Prototype {j+1} weights ({m} space-separated values): ").strip().split()]
        cls = input(f"Class label for Prototype {j+1}: ").strip()
        weights.append(row)
        proto_classes.append(cls)

    n_samples = int(input("\nNumber of training samples: "))
    samples = []
    sample_classes = []

    print(f"Enter {n_samples} training samples (features and target class label):")
    for i in range(n_samples):
        line = input(f"Sample {i+1} ([{m} features] [TargetClass]): ").strip().split()
        features = [float(x) for x in line[:m]]
        target = line[m]
        samples.append(features)
        sample_classes.append(target)

    alpha = float(input("\nEnter initial learning rate alpha (e.g., 0.1): "))
    epochs = int(input("Enter number of epochs: "))

    for epoch in range(epochs):
        for x, target in zip(samples, sample_classes):
            # 1. Find the winning prototype
            distances = [euclidean_distance(x, weights[j]) for j in range(num_proto)]
            winner = distances.index(min(distances))

            # 2. Update winner based on class agreement
            if proto_classes[winner] == target:
                for d in range(m):
                    weights[winner][d] += alpha * (x[d] - weights[winner][d])
            else:
                for d in range(m):
                    weights[winner][d] -= alpha * (x[d] - weights[winner][d])

        # Learning rate decay per epoch
        alpha *= 0.95

    print("\n" + "=" * 50)
    print("LVQ Training Completed. Final Prototype Vectors:")
    for j in range(num_proto):
        formatted = ", ".join(f"{w:.4f}" for w in weights[j])
        print(f"Prototype {j+1} (Class {proto_classes[j]}): [{formatted}]")
    print("=" * 50)

if __name__ == "__main__":
    main()