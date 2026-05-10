# 🐍 Intermediate Python Problem Set

> A curated collection of **intermediate-level Python problems** with clean solutions, full test coverage, and real-world concepts — ready to study and extend.

---

## 📚 Topics Covered

| # | Topic | Concepts |
|---|-------|----------|
| 1 | String Manipulation | Palindrome, Caesar Cipher, Anagram |
| 2 | List Comprehensions | Flatten, Primes (Sieve), Group By |
| 3 | Recursion | Factorial, Fibonacci, Binary Search |
| 4 | OOP | BankAccount, Stack, Queue |
| 5 | Decorators | `@timer`, `@retry` factory |
| 6 | Generators | Fibonacci stream, Running Average |
| 7 | Functional Programming | `map`, `filter`, `lambda`, `sorted` |
| 8 | Error Handling | `try/except`, custom raises |
| 9 | File Handling | Read, Write, Word Frequency |
| 10 | Matrix Operations | Transpose, Matrix Multiply |

---

## 📁 Project Structure

```
python_intermediate/
├── solutions/
│   └── problems.py        # All solutions with docstrings
├── tests/
│   └── test_problems.py   # Full test suite (pytest)
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/python-intermediate.git
cd python-intermediate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the tests
```bash
# Using pytest (recommended)
pytest tests/test_problems.py -v

# Without pytest
python tests/test_problems.py
```

---

## 🔍 Example Usage

```python
from solutions.problems import (
    caesar_cipher, primes_up_to, BankAccount,
    fibonacci_generator, apply_discount
)

# Caesar Cipher
print(caesar_cipher("Hello World", 3))   # → "Khoor Zruog"

# Primes up to 50
print(primes_up_to(50))  # → [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Bank Account
acc = BankAccount("Alice", balance=1000)
acc.deposit(500)
acc.withdraw(200)
acc.statement()

# Fibonacci Generator
for num in fibonacci_generator(100):
    print(num, end=" ")  # → 0 1 1 2 3 5 8 13 21 34 55 89

# Apply discount
print(apply_discount([100, 250, 399], 10))  # → [90.0, 225.0, 359.1]
```

---

## 🧪 Test Results

```
PASSED  TestStringManipulation::test_palindrome_basic
PASSED  TestStringManipulation::test_palindrome_with_spaces
PASSED  TestStringManipulation::test_caesar_cipher
PASSED  TestStringManipulation::test_anagram_true
...
PASSED  TestMatrix::test_transpose
PASSED  TestMatrix::test_matrix_multiply
======================== 30 passed in 0.12s ========================
```

---

## 💡 How to Use This Repo

- **Studying?** Read `solutions/problems.py` — every function has a docstring.
- **Practicing?** Delete the function body and try solving it yourself before peeking.
- **Extending?** Fork it, add your own problems, and submit a PR!

---

## 📦 Requirements

- Python 3.8+
- `pytest` (for running tests)

---

## 🤝 Contributing

1. Fork this repo
2. Add a new problem in `solutions/problems.py`
3. Add tests in `tests/test_problems.py`
4. Submit a Pull Request

---

## 📝 License

MIT License — free to use, modify, and share.

---

*Made with ❤️ for Python learners*
