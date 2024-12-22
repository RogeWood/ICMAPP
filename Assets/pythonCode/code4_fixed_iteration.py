##code4(input(1~10) output a picture)
import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial and fixed point function
f = np.poly1d([1, -4, 3.5])

# Fixed-point iteration function
g = lambda x: x - f(x)

# Main program
if __name__ == "__main__":
    print("\nFinding a Fixed Point\n")

    try:
        # User input for number of iterations (1 to 10)
        num_iterations = int(input("Please enter the number of iterations (1 to 10):\n").strip())
        if not (1 <= num_iterations <= 10):
            raise ValueError("Number of iterations must be between 1 and 10.")

        # Initialize the plot
        fig, ax = plt.subplots()

        # Plot the function and identity line
        xx = np.linspace(2, 3, 400)
        ax.plot(xx, g(xx), label="y=g(x)")
        ax.plot(xx, xx, label="y=x")
        plt.axis("equal")
        plt.legend()
        plt.title("Finding a Fixed Point")

        # Initial guess
        x = 2.1
        y = g(x)

        # Perform fixed-point iterations
        for k in range(num_iterations):
            ax.plot([x, x], [x, y], "r--")  # Vertical line
            ax.plot([x, y], [y, y], "k--")  # Horizontal line
            x = y  # Update x
            y = g(x)  # Compute new y

        # Show the plot
        plt.savefig("fixed_point_iterations.png")
        print("\nFixed point iterations saved as 'fixed_point_iterations.png'.")
        plt.show()

    except ValueError as e:
        print(f"\nError: {e}")


def fixed_iteration_main(inputString):
    try:
        # User input for number of iterations (1 to 10)
        num_iterations = int(inputString.strip())
        if not (1 <= num_iterations <= 10):
            raise ValueError("Number of iterations must be between 1 and 10.")

        # Initialize the plot
        fig, ax = plt.subplots()

        # Plot the function and identity line
        xx = np.linspace(2, 3, 400)
        ax.plot(xx, g(xx), label="y=g(x)")
        ax.plot(xx, xx, label="y=x")
        plt.axis("equal")
        plt.legend()
        plt.title("Finding a Fixed Point")

        # Initial guess
        x = 2.1
        y = g(x)

        # Perform fixed-point iterations
        for k in range(num_iterations):
            ax.plot([x, x], [x, y], "r--")  # Vertical line
            ax.plot([x, y], [y, y], "k--")  # Horizontal line
            x = y  # Update x
            y = g(x)  # Compute new y

        # Show the plot
        plt.savefig("fixed_point_iterations.png")
        print("\nFixed point iterations saved as 'fixed_point_iterations.png'.")
        plt.show()

    except ValueError as e:
        print(f"\nError: {e}")