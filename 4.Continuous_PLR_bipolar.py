import math

n = int(input("Number of training examples: "))
m = int(input("Number of inputs per example: "))

inputs = []
targets = []
weights = []

print("\nEnter input values, one number at a time:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(float(input(f"Input x[{i+1}][{j+1}]: ")))
    inputs.append(row)

print("\nEnter target outputs (continuous values between -1 and 1):")
for i in range(n):
    targets.append(float(input(f"Target d[{i+1}]: ")))

print("\nEnter initial weights, one at a time:")
for j in range(m):
    weights.append(float(input(f"Initial weight w[{j+1}]: ")))

bias = float(input("Initial bias: "))
rate = float(input("Learning rate (c / eta): "))
max_epochs = int(input("Maximum number of epochs: "))
error_threshold = float(input("Error convergence threshold (e.g., 0.05): "))

for epoch in range(max_epochs):
    errors = 0.0

    for i in range(n):
        x = inputs[i]
        target = targets[i]

        net = bias
        for j in range(m):
            net += weights[j] * x[j]

        # Bipolar continuous activation (tanh)
        output = math.tanh(net)
        error = target - output
        derivative = 1.0 - output ** 2

        # Delta rule: delta_w = rate * (d - y) * f'(net) * x
        for j in range(m):
            weights[j] += rate * error * derivative * x[j]
        bias += rate * error * derivative

        errors += abs(error)

    if (errors / n) < error_threshold:
        print(f"\nTraining converged in epoch {epoch + 1} with avg error {errors / n:.5f}")
        break
else:
    print(f"\nTraining did not reach threshold within {max_epochs} epochs. Final avg error: {errors / n:.5f}")

print("Final weights:", weights)
print("Final bias:", bias)