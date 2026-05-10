"""
=====================================
  TOPIC 5 — DECORATORS
=====================================
What is a Decorator?
  A decorator is a function that WRAPS
  another function to add extra behaviour
  without changing its original code.

  Think of it like a phone case —
  the phone (function) stays the same,
  but the case adds protection (extra feature).

Decorators Here:
  1. @timer      — measures execution time
  2. @logger     — logs function calls
  3. @retry      — retries on failure
  4. @validate_positive — input validation
=====================================
"""

import functools
import time


# ─────────────────────────────────────
# DECORATOR 1: Timer
# ─────────────────────────────────────
# Prints how long a function took to run.

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[Timer] '{func.__name__}' took {end - start:.6f} seconds")
        return result
    return wrapper


# ─────────────────────────────────────
# DECORATOR 2: Logger
# ─────────────────────────────────────
# Logs every time a function is called, with its arguments.

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[Log] Calling '{func.__name__}' with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[Log] '{func.__name__}' returned {result}")
        return result
    return wrapper


# ─────────────────────────────────────
# DECORATOR 3: Retry Factory
# ─────────────────────────────────────
# Retries a failing function up to `times` attempts.

def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry] Attempt {attempt}/{times} failed: {e}")
            raise RuntimeError(f"'{func.__name__}' failed after {times} retries.")
        return wrapper
    return decorator


# ─────────────────────────────────────
# DECORATOR 4: Validate Positive Input
# ─────────────────────────────────────
# Raises ValueError if any argument is not positive.

def validate_positive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative input {arg} not allowed in '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper


# ─────────────────────────────────────
# USING THE DECORATORS
# ─────────────────────────────────────

@timer
def slow_sum(n: int) -> int:
    """Sum of 1..n (deliberately slow)."""
    total = 0
    for i in range(n):
        total += i
    return total


@logger
def add(a: int, b: int) -> int:
    return a + b


@retry(times=3)
def unreliable_function(fail_count: list):
    """Fails the first 2 times, succeeds on the 3rd."""
    if fail_count[0] < 2:
        fail_count[0] += 1
        raise ConnectionError("Server not ready.")
    return "Success!"


@validate_positive
@timer
def square_root(n: float) -> float:
    return n ** 0.5


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 5 — DECORATORS")
    print("=" * 40)

    print("\n[1] @timer")
    result = slow_sum(1_000_000)
    print(f"Result: {result}")

    print("\n[2] @logger")
    add(10, 25)

    print("\n[3] @retry")
    fail_count = [0]
    print(unreliable_function(fail_count))

    print("\n[4] @validate_positive + @timer stacked")
    print(f"√144 = {square_root(144)}")

    print("\n[4b] Negative input — should raise error")
    try:
        square_root(-9)
    except ValueError as e:
        print(f"Caught: {e}")
