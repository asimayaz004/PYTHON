"""
=====================================
  TOPIC 3 — RECURSION
=====================================
Problems:
  1. Factorial
  2. Fibonacci Number
  3. Power (base ^ exponent)
  4. Sum of Digits
  5. Binary Search (recursive)
  6. Reverse a String (recursive)
=====================================
"""


# ─────────────────────────────────────
# PROBLEM 1: Factorial
# ─────────────────────────────────────
# 5! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)


# ─────────────────────────────────────
# PROBLEM 2: Fibonacci Number
# ─────────────────────────────────────
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# fibonacci(7) = 13

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ─────────────────────────────────────
# PROBLEM 3: Power
# ─────────────────────────────────────
# power(2, 10) = 1024
# power(2, -2) = 0.25

def power(base: float, exp: int) -> float:
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


# ─────────────────────────────────────
# PROBLEM 4: Sum of Digits
# ─────────────────────────────────────
# sum_of_digits(1234) = 1+2+3+4 = 10

def sum_of_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


# ─────────────────────────────────────
# PROBLEM 5: Binary Search
# ─────────────────────────────────────
# Works only on SORTED lists.
# Returns the index of target, or -1 if not found.

def binary_search(arr: list, target, low=None, high=None) -> int:
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


# ─────────────────────────────────────
# PROBLEM 6: Reverse a String
# ─────────────────────────────────────
# reverse_string("hello") → "olleh"

def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 3 — RECURSION")
    print("=" * 40)

    print("\n[1] Factorial")
    print(factorial(5))                              # 120
    print(factorial(0))                              # 1

    print("\n[2] Fibonacci")
    print(fibonacci(7))                              # 13
    print([fibonacci(i) for i in range(10)])         # [0,1,1,2,3,5,8,13,21,34]

    print("\n[3] Power")
    print(power(2, 10))                              # 1024
    print(power(2, -2))                              # 0.25

    print("\n[4] Sum of Digits")
    print(sum_of_digits(1234))                       # 10
    print(sum_of_digits(9999))                       # 36

    print("\n[5] Binary Search")
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))                     # 3 (index)
    print(binary_search(arr, 4))                     # -1 (not found)

    print("\n[6] Reverse String")
    print(reverse_string("hello"))                   # olleh
    print(reverse_string("Python"))                  # nohtyP
