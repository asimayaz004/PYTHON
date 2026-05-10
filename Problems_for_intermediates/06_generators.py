"""
=====================================
  TOPIC 6 — GENERATORS
=====================================
What is a Generator?
  A generator is a function that produces
  values ONE AT A TIME using `yield`.
  It does NOT store everything in memory.

  Think of it like a water tap —
  you get water only when you turn it on,
  not all at once in a bucket.

Problems:
  1. Fibonacci Generator
  2. Custom Range Generator
  3. Running Average
  4. Infinite Counter
  5. Read Large File Line by Line
=====================================
"""


# ─────────────────────────────────────
# GENERATOR 1: Fibonacci Sequence
# ─────────────────────────────────────
# Yields Fibonacci numbers up to `limit`.

def fibonacci_generator(limit: int):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# ─────────────────────────────────────
# GENERATOR 2: Custom Range
# ─────────────────────────────────────
# Like Python's built-in range(), but yours.

def my_range(start: int, stop: int, step: int = 1):
    current = start
    while current < stop:
        yield current
        current += step


# ─────────────────────────────────────
# GENERATOR 3: Running Average
# ─────────────────────────────────────
# Yields the running average after each new value.
# Input:  [10, 20, 30]
# Output: 10.0, 15.0, 20.0

def running_average(data: list):
    total = 0
    for i, val in enumerate(data, 1):
        total += val
        yield total / i


# ─────────────────────────────────────
# GENERATOR 4: Infinite Counter
# ─────────────────────────────────────
# Counts forever — you decide when to stop.

def infinite_counter(start: int = 0, step: int = 1):
    current = start
    while True:
        yield current
        current += step


# ─────────────────────────────────────
# GENERATOR 5: Read File Line by Line
# ─────────────────────────────────────
# Memory-efficient — doesn't load whole file.

def read_lines(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 6 — GENERATORS")
    print("=" * 40)

    print("\n[1] Fibonacci up to 100")
    print(list(fibonacci_generator(100)))
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    print("\n[2] Custom Range (0 to 20, step 3)")
    print(list(my_range(0, 20, 3)))
    # [0, 3, 6, 9, 12, 15, 18]

    print("\n[3] Running Average of [10, 20, 30, 40]")
    print(list(running_average([10, 20, 30, 40])))
    # [10.0, 15.0, 20.0, 25.0]

    print("\n[4] Infinite Counter — first 8 even numbers")
    counter = infinite_counter(start=0, step=2)
    result = [next(counter) for _ in range(8)]
    print(result)
    # [0, 2, 4, 6, 8, 10, 12, 14]

    print("\n[5] Generator expression (squares of evens up to 20)")
    gen = (x**2 for x in range(1, 21) if x % 2 == 0)
    print(list(gen))
    # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
