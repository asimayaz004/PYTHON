"""
=====================================
  TOPIC 7 — ERROR HANDLING
=====================================
Concepts:
  1. try / except / else / finally
  2. Raising custom exceptions
  3. Multiple exception types
  4. Safe wrappers for common operations

Problems:
  1. Safe Division
  2. Safe Integer Parse
  3. Custom AgeError exception
  4. File reading with error handling
  5. Input validator with multiple checks
=====================================
"""


# ─────────────────────────────────────
# PROBLEM 1: Safe Division
# ─────────────────────────────────────

def safe_divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except TypeError:
        raise TypeError("Both inputs must be numbers.")


# ─────────────────────────────────────
# PROBLEM 2: Safe Integer Parse
# ─────────────────────────────────────
# Returns None instead of crashing.

def safe_int_parse(value: str):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


# ─────────────────────────────────────
# PROBLEM 3: Custom Exception
# ─────────────────────────────────────

class AgeError(Exception):
    """Raised when an age value is invalid."""
    pass


def validate_age(age: int) -> str:
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise AgeError("Age cannot be negative.")
    if age > 150:
        raise AgeError("Age seems unrealistically high.")
    return f"Valid age: {age}"


# ─────────────────────────────────────
# PROBLEM 4: Safe File Read
# ─────────────────────────────────────

def safe_read_file(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"[Error] File not found: {filepath}"
    except PermissionError:
        return f"[Error] No permission to read: {filepath}"


# ─────────────────────────────────────
# PROBLEM 5: Full try/except/else/finally
# ─────────────────────────────────────
# else  → runs only if NO exception occurred
# finally → ALWAYS runs (cleanup code)

def connect_and_process(data: dict, key: str):
    print(f"Trying to get '{key}' from data...")
    try:
        value = data[key]
        result = int(value) * 2
    except KeyError:
        print(f"  [except] Key '{key}' not found in data.")
    except ValueError:
        print(f"  [except] Value '{value}' cannot be converted to int.")
    else:
        print(f"  [else] Success! Result = {result}")
    finally:
        print("  [finally] Cleanup done — always runs.\n")


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 7 — ERROR HANDLING")
    print("=" * 40)

    print("\n[1] Safe Division")
    print(safe_divide(10, 2))          # 5.0
    try:
        safe_divide(5, 0)
    except ZeroDivisionError as e:
        print(f"Caught: {e}")

    print("\n[2] Safe Integer Parse")
    print(safe_int_parse("42"))        # 42
    print(safe_int_parse("hello"))     # None
    print(safe_int_parse(None))        # None

    print("\n[3] Custom AgeError")
    print(validate_age(25))
    try:
        validate_age(-5)
    except AgeError as e:
        print(f"Caught AgeError: {e}")
    try:
        validate_age(200)
    except AgeError as e:
        print(f"Caught AgeError: {e}")

    print("\n[4] Safe File Read")
    print(safe_read_file("nonexistent.txt"))

    print("\n[5] try / except / else / finally")
    data = {"score": "88", "name": "Alice", "grade": "B+"}
    connect_and_process(data, "score")    # success path
    connect_and_process(data, "grade")    # ValueError (can't int("B+"))
    connect_and_process(data, "age")      # KeyError (missing key)
