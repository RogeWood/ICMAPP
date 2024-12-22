##code6(input(float)input(float) output(string))
from scipy.optimize import newton
import numpy as np

# Example function
def example_function(x):
    # Example: f(x) = x - (x-1)*(x-100)
    return x - (x - 1) * (x - 100)

# # Main program
# if __name__ == "__main__":
#     print("\nSecant Method Using scipy.optimize.newton\n")

#     try:
#         # User input for initial guesses
#         x0 = float(input("Please enter the first initial guess x0:").strip())
#         x1 = float(input("Please enter the second initial guess x1:").strip())

#         # Perform the secant method using scipy's newton method
#         root = newton(example_function, x0, tol=1e-6, maxiter=100, x1=x1)

#         print(f"\nRoot found: {root}")

#     except Exception as e:
#         print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")


def secent_method_main(inputString):
    try:
        a, b = inputString.split('|')
        # User input for initial guesses
        x0 = float(a.strip())
        x1 = float(b.strip())

        # Perform the secant method using scipy's newton method
        root = newton(example_function, x0, tol=1e-6, maxiter=100, x1=x1)

        output = f"\nRoot found: {root}"
        print(f"\nRoot found: {root}")
        return output

    except Exception as e:
        print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")
        output = f"\nError: {e}. Please ensure your inputs are correctly formatted.\n"
        return output