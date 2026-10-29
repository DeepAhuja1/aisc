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

print("\nEnter target outputs (-1 or 1), one at a time:")
for i in range(n):
    targets.append(float(input(f"Target d[{i+1}]: ")))

print("\nEnter initial weights, one at a time:")
for j in range(m):
    weights.append(float(input(f"Initial weight w[{j+1}]: ")))

bias = float(input("Initial bias: "))
rate = float(input("Learning rate (c / eta): "))
max_epochs = int(input("Maximum number of epochs: "))

for epoch in range(max_epochs):
    errors = 0

    for i in range(n):
        x = inputs[i]
        target = targets[i]

        net = bias
        for j in range(m):
            net += weights[j] * x[j]

        # Bipolar binary activation function: f(net) = 1 if net >= 0 else -1
        output = 1.0 if net >= 0 else -1.0
        error = target - output

        for j in range(m):
            weights[j] += rate * error * x[j]
        bias += rate * error

        errors += abs(error)

    if errors == 0:
        print(f"\nTraining converged in epoch {epoch + 1}")
        break
else:
    print(f"\nTraining did not converge within {max_epochs} epochs")

print("Final weights:", weights)
print("Final bias:", bias)