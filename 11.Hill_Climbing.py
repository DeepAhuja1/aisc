MAX = 10
MAX_ITERATIONS = 1000

def evaluate_function(x, a, degree):
    result = 0.0
    for i in range(degree + 1):
        result = result * x + a[i]
    return result

def main():
    print("--- Hill Climbing Maximization ---")

    degree = int(input("Enter degree of function: "))

    if degree < 0 or degree >= MAX:
        print(f"Invalid degree. Enter a degree between 0 and {MAX - 1}.")
        return

    print("Enter coefficients from highest power to constant:")
    a = []
    for i in range(degree + 1):
        coef = float(input(f"Coefficient a[{degree - i}]: "))
        a.append(coef)

    x = float(input("Enter starting value of x: "))
    step = float(input("Enter step size: "))

    if step <= 0:
        print("Step size must be greater than 0.")
        return

    current = evaluate_function(x, a, degree)
    iteration = 0

    print(f"\nIteration {iteration}")
    print(f"x = {x:.4f}")
    print(f"f(x) = {current:.4f}")

    while iteration < MAX_ITERATIONS:
        left = x - step
        right = x + step

        left_value = evaluate_function(left, a, degree)
        right_value = evaluate_function(right, a, degree)

        print("\nChecking neighbours:")
        print(f"  Left  : x = {left:.4f}   f(x) = {left_value:.4f}")
        print(f"  Right : x = {right:.4f}   f(x) = {right_value:.4f}")

        if left_value > current and left_value >= right_value:
            x = left
            current = left_value
        elif right_value > current:
            x = right
            current = right_value
        else:
            print("\nNo better neighbour found.")
            print("Local maximum reached.")
            print(f"Final x = {x:.4f}")
            print(f"Maximum value = {current:.4f}")
            break

        iteration += 1

        print("Moving to better neighbour")
        print(f"Iteration {iteration}")
        print(f"x = {x:.4f}")
        print(f"f(x) = {current:.4f}")

    if iteration >= MAX_ITERATIONS:
        print("\nMaximum iteration limit reached.")
        print("The function may not have a finite local maximum or step size is too small.")
        print(f"Current x = {x:.4f}")
        print(f"Current value = {current:.4f}")

if __name__ == "__main__":
    main()