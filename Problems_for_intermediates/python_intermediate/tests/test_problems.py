"""
=====================================
🧪 Test Suite for Intermediate Python
=====================================
Run with:  python -m pytest tests/test_problems.py -v
Or:        python tests/test_problems.py
=====================================
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from solutions.problems import (
    is_palindrome, count_vowels_consonants, caesar_cipher, anagram_check,
    flatten_list, primes_up_to, group_by_length,
    factorial, fibonacci, power, binary_search,
    BankAccount, Stack, Queue,
    fibonacci_generator, running_average,
    apply_discount, filter_even, sort_by_second,
    safe_divide, safe_int_parse,
    transpose, matrix_multiply,
)


# ── STRING ──────────────────────────

class TestStringManipulation:
    def test_palindrome_basic(self):
        assert is_palindrome("racecar") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_vowels_consonants(self):
        result = count_vowels_consonants("Hello World")
        assert result["vowels"] == 3
        assert result["consonants"] == 7

    def test_caesar_cipher(self):
        assert caesar_cipher("abc", 3) == "def"
        assert caesar_cipher("xyz", 3) == "abc"
        assert caesar_cipher("Hello!", 1) == "Ifmmp!"

    def test_anagram_true(self):
        assert anagram_check("listen", "silent") is True

    def test_anagram_false(self):
        assert anagram_check("hello", "world") is False


# ── LISTS & FUNCTIONAL ───────────────

class TestListOperations:
    def test_flatten(self):
        assert flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    def test_primes(self):
        assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    def test_primes_small(self):
        assert primes_up_to(1) == []

    def test_group_by_length(self):
        result = group_by_length(["cat", "dog", "elephant", "ant"])
        assert set(result[3]) == {"cat", "dog", "ant"}
        assert result[8] == ["elephant"]

    def test_filter_even(self):
        assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_sort_by_second(self):
        assert sort_by_second([(1, 3), (2, 1), (3, 2)]) == [(2, 1), (3, 2), (1, 3)]

    def test_apply_discount(self):
        assert apply_discount([100, 200, 300], 10) == [90.0, 180.0, 270.0]


# ── RECURSION ────────────────────────

class TestRecursion:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1
        assert fibonacci(7) == 13

    def test_power(self):
        assert power(2, 10) == 1024
        assert power(3, 0) == 1
        assert power(2, -2) == 0.25

    def test_binary_search_found(self):
        arr = [1, 3, 5, 7, 9, 11]
        assert binary_search(arr, 7) == 3

    def test_binary_search_not_found(self):
        arr = [1, 3, 5, 7, 9]
        assert binary_search(arr, 4) == -1


# ── OOP ──────────────────────────────

class TestBankAccount:
    def setup_method(self):
        self.acc = BankAccount("Alice", 1000)

    def test_initial_balance(self):
        assert self.acc.balance == 1000

    def test_deposit(self):
        self.acc.deposit(500)
        assert self.acc.balance == 1500

    def test_withdraw(self):
        self.acc.withdraw(200)
        assert self.acc.balance == 800

    def test_insufficient_funds(self):
        with pytest.raises(ValueError, match="Insufficient"):
            self.acc.withdraw(5000)

    def test_invalid_deposit(self):
        with pytest.raises(ValueError):
            self.acc.deposit(-100)


class TestStack:
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek(self):
        s = Stack()
        s.push(42)
        assert s.peek() == 42
        assert s.size() == 1

    def test_pop_empty(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()


class TestQueue:
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        assert q.dequeue() == "a"
        assert q.dequeue() == "b"

    def test_dequeue_empty(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()


# ── GENERATORS ───────────────────────

class TestGenerators:
    def test_fibonacci_generator(self):
        result = list(fibonacci_generator(20))
        assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21]

    def test_running_average(self):
        result = list(running_average([10, 20, 30]))
        assert result == [10.0, 15.0, 20.0]


# ── ERROR HANDLING ───────────────────

class TestErrorHandling:
    def test_safe_divide(self):
        assert safe_divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            safe_divide(5, 0)

    def test_safe_int_parse_valid(self):
        assert safe_int_parse("42") == 42

    def test_safe_int_parse_invalid(self):
        assert safe_int_parse("abc") is None


# ── MATRIX ───────────────────────────

class TestMatrix:
    def test_transpose(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert transpose(m) == [[1, 4], [2, 5], [3, 6]]

    def test_matrix_multiply(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        assert matrix_multiply(A, B) == [[19, 22], [43, 50]]

    def test_matrix_multiply_dimension_error(self):
        with pytest.raises(ValueError):
            matrix_multiply([[1, 2]], [[1, 2]])


# ── RUN WITHOUT PYTEST ───────────────

if __name__ == "__main__":
    import traceback

    tests = [
        TestStringManipulation, TestListOperations, TestRecursion,
        TestBankAccount, TestStack, TestQueue,
        TestGenerators, TestErrorHandling, TestMatrix,
    ]

    passed = failed = 0
    for cls in tests:
        instance = cls()
        for name in dir(cls):
            if name.startswith("test_"):
                method = getattr(instance, name)
                if hasattr(instance, "setup_method"):
                    instance.setup_method()
                try:
                    method()
                    print(f"  ✅ {cls.__name__}.{name}")
                    passed += 1
                except Exception as e:
                    print(f"  ❌ {cls.__name__}.{name} → {e}")
                    failed += 1

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*40}")
