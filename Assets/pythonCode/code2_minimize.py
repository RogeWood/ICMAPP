##code2
import numpy as np

# Function to solve Ax = b using least squares
def minimize_ax_b(A, b):
    # Compute the least squares solution
    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    return x, residuals

# Main program
# if __name__ == "__main__":
#     print("\nMinimizing ||Ax - b||\n")

#     try:
#         # User input for matrix A
#         A = input("Please enter matrix A (rows separated by semicolons, elements separated by commas, e.g., '1,2;3,4'):\n").strip()
#         A = np.array([list(map(float, row.split(","))) for row in A.split(";")])

#         # User input for vector b
#         b = input("Please enter vector b (elements separated by commas, e.g., '5,6'):\n").strip()
#         b = np.array(list(map(float, b.split(","))))

#         # Ensure dimensions match
#         if A.shape[0] != b.shape[0]:
#             raise ValueError("The number of rows in A must match the length of b.")

#         # Solve the least squares problem
#         x, residuals = minimize_ax_b(A, b)

#         print(f"\nSolution x:\n{x}")
#         if residuals.size > 0:
#             print(f"\nResidual ||Ax - b||^2:\n{residuals[0]}")
#         else:
#             print("\nNo residuals (exact solution).")

#     except Exception as e:
#         print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")

def minimize_main(inputString):
    try:
        A, b = inputString.split("|")
        # User input for matrix A
        A = A.strip()
        A = np.array([list(map(float, row.split(","))) for row in A.split(";")])

        # User input for vector b
        b = b.strip()
        b = np.array(list(map(float, b.split(","))))

        output = ""
        # Ensure dimensions match
        if A.shape[0] != b.shape[0]:
            output += "The number of rows in A must match the length of b."
            raise ValueError("The number of rows in A must match the length of b.")

        # Solve the least squares problem
        x, residuals = minimize_ax_b(A, b)

        output += f"\nSolution x:\n{x}"
        print(f"\nSolution x:\n{x}")
        if residuals.size > 0:
            print(f"\nResidual ||Ax - b||^2:\n{residuals[0]}")
            output += f"\nResidual ||Ax - b||^2:\n{residuals[0]}"
        else:
            print("\nNo residuals (exact solution).")
            output += "\nNo residuals (exact solution)."
        
        output = f"\nError: {e}. Please ensure your inputs are correctly formatted.\n"

    except Exception as e:
        print(f"\nError: {e}. Please ensure your inputs are correctly formatted.\n")
        output = f"\nError: {e}. Please ensure your inputs are correctly formatted.\n"
        return output