#code3
import numpy as np

# QR Factorization function
def qr_factorization(A):
    Q, R = np.linalg.qr(A)
    return Q, R

# # Main program
# if __name__ == "__main__":
#     print("\nQR Factorization\n")

#     try:
#         # User input for matrix A
#         A = input("Please enter matrix A (rows separated by semicolons, elements by commas, e.g., '1,2;3,4'):\n").strip()
#         A = np.array([list(map(float, row.split(","))) for row in A.split(";")])

#         # Perform QR factorization
#         Q, R = qr_factorization(A)

#         print("\nMatrix Q (Orthogonal):\n", Q)
#         print("\nMatrix R (Upper Triangular):\n", R)

#     except ValueError:
#         print("\nInvalid input! Please ensure correct formatting and numerical values.\n")

def QRfactor_main(inputString):
    try:
        # User input for matrix A
        A = inputString.strip()
        A = np.array([list(map(float, row.split(","))) for row in A.split(";")])

        # Perform QR factorization
        Q, R = qr_factorization(A)

        output = f"\nMatrix Q (Orthogonal):\n {Q}\n\n"
        output += f"\nMatrix R (Upper Triangular):\n {R}\n"
        print("\nMatrix Q (Orthogonal):\n", Q)
        print("\nMatrix R (Upper Triangular):\n", R)
        return output
    except ValueError:
        print("\nInvalid input! Please ensure correct formatting and numerical values.\n")
        output = "\nInvalid input! Please ensure correct formatting and numerical values.\n"
        return output