"""
=====================================
🐍 Intermediate Python Problem Set
=====================================
Topics Covered:
  - String Manipulation
  - List Comprehensions
  - Recursion
  - OOP (Classes & Objects)
  - File Handling
  - Error Handling
  - Decorators
  - Generators
  - Lambda & Functional Programming
  - Data Structures (Stack, Queue)
=====================================
"""

import functools
import time
from collections import deque, Counter


# ─────────────────────────────────────
# 1. STRING MANIPULATION
# ─────────────────────────────────────

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignores case and spaces)."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels_consonants(s: str) -> dict:
    """Return count of vowels and consonants in a string."""
    vowels = set("aeiouAEIOU")
    result = {"vowels": 0, "consonants": 0}
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                result["vowels"] += 1
            else:
                result["consonants"] += 1
    return result


def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def anagram_check(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    return Counter(s1.lower()) == Counter(s2.lower())


# ─────────────────────────────────────
# 2. LIST COMPREHENSIONS & FUNCTIONAL
# ─────────────────────────────────────

def flatten_list(nested: list) -> list:
    """Flatten a nested list (one level deep)."""
    return [item for sublist in nested for item in sublist]


def primes_up_to(n: int) -> list:
    """Return all prime numbers up to n using list comprehension + sieve."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def group_by_length(words: list) -> dict:
    """Group words by their length."""
    result = {}
    for word in words:
        result.setdefault(len(word), []).append(word)
    return result


# ─────────────────────────────────────
# 3. RECURSION
# ─────────────────────────────────────

def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number recursively."""
    if n < 0:
        raise ValueError("n must be non-negative.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base: float, exp: int) -> float:
    """Compute base^exp recursively."""
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


def binary_search(arr: list, target, low=None, high=None) -> int:
    """Recursive binary search. Returns index or -1 if not found."""
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
# 4. OBJECT-ORIENTED PROGRAMMING
# ─────────────────────────────────────

class BankAccount:
    """Simple bank account with deposit, withdraw, and history."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._history.append(f"Deposited: ₹{amount:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self._history.append(f"Withdrew: ₹{amount:.2f}")

    @property
    def balance(self):
        return self._balance

    def statement(self):
        print(f"\n--- Statement for {self.owner} ---")
        for entry in self._history:
            print(f"  {entry}")
        print(f"  Current Balance: ₹{self._balance:.2f}\n")


class Stack:
    """Stack data structure using a list."""

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)


class Queue:
    """Queue data structure using deque."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self._data.popleft()

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)


# ─────────────────────────────────────
# 5. DECORATORS
# ─────────────────────────────────────

def timer(func):
    """Decorator that prints how long a function takes to run."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[Timer] {func.__name__}() took {end - start:.6f} seconds")
        return result
    return wrapper


def retry(times=3):
    """Decorator factory: retries a function up to `times` on exception."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Retry] Attempt {attempt} failed: {e}")
            raise RuntimeError(f"Function '{func.__name__}' failed after {times} retries.")
        return wrapper
    return decorator


# ─────────────────────────────────────
# 6. GENERATORS
# ─────────────────────────────────────

def fibonacci_generator(limit: int):
    """Yield Fibonacci numbers up to `limit`."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def range_generator(start: int, stop: int, step: int = 1):
    """Custom range generator."""
    current = start
    while current < stop:
        yield current
        current += step


def running_average(data: list):
    """Generator that yields the running average of a list."""
    total = 0
    for i, val in enumerate(data, 1):
        total += val
        yield total / i


# ─────────────────────────────────────
# 7. LAMBDA & FUNCTIONAL PROGRAMMING
# ─────────────────────────────────────

def apply_discount(prices: list, discount_pct: float) -> list:
    """Apply a discount percentage to a list of prices."""
    apply = lambda price: round(price * (1 - discount_pct / 100), 2)
    return list(map(apply, prices))


def filter_even(numbers: list) -> list:
    return list(filter(lambda x: x % 2 == 0, numbers))


def sort_by_second(tuples: list) -> list:
    """Sort a list of tuples by the second element."""
    return sorted(tuples, key=lambda t: t[1])


# ─────────────────────────────────────
# 8. ERROR HANDLING
# ─────────────────────────────────────

def safe_divide(a: float, b: float) -> float:
    """Divide a by b with proper error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
    except TypeError as e:
        raise TypeError(f"Invalid types for division: {e}")


def safe_int_parse(value: str) -> int:
    """Safely parse a string to int, returning None on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


# ─────────────────────────────────────
# 9. FILE HANDLING
# ─────────────────────────────────────

def write_to_file(filepath: str, content: str, mode: str = "w") -> None:
    """Write content to a file."""
    with open(filepath, mode, encoding="utf-8") as f:
        f.write(content)


def read_file(filepath: str) -> str:
    """Read and return file contents."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def word_frequency_from_file(filepath: str) -> dict:
    """Count word frequency in a text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        words = f.read().lower().split()
    return dict(Counter(words))


# ─────────────────────────────────────
# 10. MATRIX OPERATIONS
# ─────────────────────────────────────

def transpose(matrix: list) -> list:
    """Transpose a 2D matrix."""
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A: list, B: list) -> list:
    """Multiply two matrices A and B."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Matrix dimensions don't match for multiplication.")
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
