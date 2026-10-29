import math

n = int(input("Number of training examples: "))
m = int(input("Number of inputs per example: "))

inputs = []
weights = []

print("\nEnter input values, one number at a time:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(float(input(f"Input x[{i+1}][{j+1}]: ")))
    inputs.append(row)

print("\nEnter initial weights, one at a time:")
for j in range(m):
    weights.append(float(input(f"Initial weight w[{j+1}]: ")))

bias = float(input("Initial bias: "))
rate = float(input("Learning rate (c / eta): "))
epochs = int(input("Number of epochs: "))

for epoch in range(epochs):
    for i in range(n):
        x = inputs[i]

        net = bias
        for j in range(m):
            net += weights[j] * x[j]

        # Bipolar continuous activation (tanh)
        output = math.tanh(net)

        # Hebbian rule: delta_w = rate * y * x
        for j in range(m):
            weights[j] += rate * output * x[j]
        bias += rate * output

print("\nTraining completed")
print("Final weights:", weights)
print("Final bias:", bias)