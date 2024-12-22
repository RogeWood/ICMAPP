##code5(input(float),output(string))
import numpy as np

# Fixed point iteration function
def fixed_point_iteration(g, x0, tolerance=1e-6, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        x_next = g(x)
        if abs(x_next - x) < tolerance:
            print(f"Converged to fixed point {x_next} after {i+1} iterations.")
            return x_next
        x = x_next
    print("Did not converge within the maximum number of iterations.")
    return x

# Define a fixed-point function g(x)
def example_function(x):
    # Example: g(x) = x - sin(x)
    return x - np.sin(x)

# # Main program
# if __name__ == "__main__":
#     print("\nFixed Point Iteration\n")

#     try:
#         # Initial guess
#         x0 = float(input("Please enter the initial guess x0:").strip())

#         # Perform fixed point iteration with the example function
#         fixed_point = fixed_point_iteration(example_function, x0)

#         print(f"\nFixed point: {fixed_point}")

#     except Exception as e:
#         print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")

def fixed_solve_main(inputString):
    try:
        # Initial guess
        x0 = float(inputString.strip())

        # Perform fixed point iteration with the example function
        fixed_point = fixed_point_iteration(example_function, x0)

        output = f"\nFixed point: {fixed_point}"
        print(f"\nFixed point: {fixed_point}")
        return output

    except Exception as e:
        print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")
        output = f"\nError: {e}. Please ensure your inputs are correctly formatted.\n"
        return output