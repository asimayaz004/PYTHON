"""
=====================================
  TOPIC 9 — MATRIX OPERATIONS
=====================================
Problems:
  1. Print a Matrix neatly
  2. Transpose a Matrix
  3. Add Two Matrices
  4. Multiply Two Matrices
  5. Rotate Matrix 90° Clockwise
  6. Find Row & Column Sum
=====================================
"""


# ─────────────────────────────────────
# HELPER: Print Matrix Neatly
# ─────────────────────────────────────

def print_matrix(matrix: list, label: str = "Matrix"):
    print(f"\n{label}:")
    for row in matrix:
        print("  ", row)


# ─────────────────────────────────────
# PROBLEM 1: Transpose
# ─────────────────────────────────────
# Flip rows and columns.
# [[1,2,3],    [[1,4],
#  [4,5,6]] →  [2,5],
#               [3,6]]

def transpose(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]


# ─────────────────────────────────────
# PROBLEM 2: Add Two Matrices
# ─────────────────────────────────────

def add_matrices(A: list, B: list) -> list:
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# ─────────────────────────────────────
# PROBLEM 3: Multiply Two Matrices
# ─────────────────────────────────────
# A is (m×n), B is (n×p) → Result is (m×p)

def multiply_matrices(A: list, B: list) -> list:
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply: A is {rows_A}×{cols_A}, B is {rows_B}×{cols_B}")
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result


# ─────────────────────────────────────
# PROBLEM 4: Rotate 90° Clockwise
# ─────────────────────────────────────
# [[1,2],    [[3,1],
#  [3,4]] →  [4,2]]

def rotate_90_clockwise(matrix: list) -> list:
    return [list(row) for row in zip(*matrix[::-1])]


# ─────────────────────────────────────
# PROBLEM 5: Row and Column Sums
# ─────────────────────────────────────

def row_sums(matrix: list) -> list:
    return [sum(row) for row in matrix]


def col_sums(matrix: list) -> list:
    return [sum(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 9 — MATRIX OPERATIONS")
    print("=" * 40)

    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8, 9],
         [1, 2, 3]]

    C = [[1, 2],
         [3, 4],
         [5, 6]]

    print("\n[1] Transpose of A")
    print_matrix(A, "A")
    print_matrix(transpose(A), "Transpose(A)")

    print("\n[2] A + B")
    print_matrix(add_matrices(A, B), "A + B")

    print("\n[3] A × C  (2×3 × 3×2 = 2×2)")
    print_matrix(A, "A (2×3)")
    print_matrix(C, "C (3×2)")
    print_matrix(multiply_matrices(A, C), "A × C")

    print("\n[4] Rotate 90° Clockwise")
    square = [[1, 2], [3, 4]]
    print_matrix(square, "Original")
    print_matrix(rotate_90_clockwise(square), "Rotated 90°")

    print("\n[5] Row & Column Sums of A")
    print("  Row sums:", row_sums(A))
    print("  Col sums:", col_sums(A))
