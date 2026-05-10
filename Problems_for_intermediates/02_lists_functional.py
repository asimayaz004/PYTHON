"""
=====================================
  TOPIC 2 — LIST COMPREHENSIONS
           & FUNCTIONAL PROGRAMMING
=====================================
Problems:
  1. Flatten a Nested List
  2. Primes up to N (Sieve of Eratosthenes)
  3. Group Words by Length
  4. Filter Even Numbers (using lambda)
  5. Apply Discount to Prices (map + lambda)
  6. Sort List of Tuples by Second Element
=====================================
"""

from collections import Counter


# ─────────────────────────────────────
# PROBLEM 1: Flatten a Nested List
# ─────────────────────────────────────
# Input:  [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

def flatten_list(nested: list) -> list:
    return [item for sublist in nested for item in sublist]


# ─────────────────────────────────────
# PROBLEM 2: Primes up to N
# ─────────────────────────────────────
# Uses the Sieve of Eratosthenes algorithm.

def primes_up_to(n: int) -> list:
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


# ─────────────────────────────────────
# PROBLEM 3: Group Words by Length
# ─────────────────────────────────────
# Input:  ["cat", "dog", "elephant", "ant"]
# Output: {3: ["cat", "dog", "ant"], 8: ["elephant"]}

def group_by_length(words: list) -> dict:
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result


# ─────────────────────────────────────
# PROBLEM 4: Filter Even Numbers
# ─────────────────────────────────────

def filter_even(numbers: list) -> list:
    return list(filter(lambda x: x % 2 == 0, numbers))


# ─────────────────────────────────────
# PROBLEM 5: Apply Discount to Prices
# ─────────────────────────────────────
# Input:  [100, 200, 300], discount=10%
# Output: [90.0, 180.0, 270.0]

def apply_discount(prices: list, discount_pct: float) -> list:
    return list(map(lambda p: round(p * (1 - discount_pct / 100), 2), prices))


# ─────────────────────────────────────
# PROBLEM 6: Sort Tuples by Second Element
# ─────────────────────────────────────
# Input:  [(1, 3), (2, 1), (3, 2)]
# Output: [(2, 1), (3, 2), (1, 3)]

def sort_by_second(tuples: list) -> list:
    return sorted(tuples, key=lambda t: t[1])


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 2 — LISTS & FUNCTIONAL")
    print("=" * 40)

    print("\n[1] Flatten List")
    print(flatten_list([[1, 2], [3, 4], [5]]))         # [1, 2, 3, 4, 5]

    print("\n[2] Primes up to 30")
    print(primes_up_to(30))                             # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    print("\n[3] Group by Length")
    print(group_by_length(["cat", "dog", "elephant", "ant"]))

    print("\n[4] Filter Even")
    print(filter_even([1, 2, 3, 4, 5, 6, 7, 8]))       # [2, 4, 6, 8]

    print("\n[5] Apply Discount (10%)")
    print(apply_discount([100, 200, 500], 10))          # [90.0, 180.0, 450.0]

    print("\n[6] Sort by Second Element")
    print(sort_by_second([(1, 3), (2, 1), (3, 2)]))    # [(2,1), (3,2), (1,3)]
