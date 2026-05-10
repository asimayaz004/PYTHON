"""
=====================================
  TOPIC 4 — OBJECT ORIENTED
            PROGRAMMING (OOP)
=====================================
Classes:
  1. BankAccount  — deposit, withdraw, statement
  2. Student      — grades, average, pass/fail
  3. Stack        — push, pop, peek (LIFO)
  4. Queue        — enqueue, dequeue (FIFO)
=====================================
"""

from collections import deque


# ─────────────────────────────────────
# CLASS 1: BankAccount
# ─────────────────────────────────────

class BankAccount:
    """A simple bank account with history tracking."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount
        self._history.append(f"Deposited  ₹{amount:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self._history.append(f"Withdrew   ₹{amount:.2f}")

    @property
    def balance(self):
        return self._balance

    def statement(self):
        print(f"\n--- Account Statement: {self.owner} ---")
        for entry in self._history:
            print(f"  {entry}")
        print(f"  Balance:   ₹{self._balance:.2f}")
        print("-" * 36)


# ─────────────────────────────────────
# CLASS 2: Student
# ─────────────────────────────────────

class Student:
    """Stores student info and computes grades."""

    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self) -> str:
        avg = self.average()
        if avg >= 90:   return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        elif avg >= 50: return "D"
        else:           return "F"

    def is_pass(self) -> bool:
        return all(m >= 33 for m in self.marks)

    def report(self):
        print(f"\n--- Student Report: {self.name} ---")
        print(f"  Marks  : {self.marks}")
        print(f"  Average: {self.average():.2f}")
        print(f"  Grade  : {self.grade()}")
        print(f"  Result : {'PASS ✅' if self.is_pass() else 'FAIL ❌'}")


# ─────────────────────────────────────
# CLASS 3: Stack (LIFO)
# ─────────────────────────────────────
# Last In, First Out — like a pile of plates.

class Stack:
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

    def __str__(self):
        return f"Stack{self._data} ← top"


# ─────────────────────────────────────
# CLASS 4: Queue (FIFO)
# ─────────────────────────────────────
# First In, First Out — like a ticket line.

class Queue:
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

    def __str__(self):
        return f"Queue{list(self._data)} → front"


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 4 — OOP")
    print("=" * 40)

    print("\n[1] BankAccount")
    acc = BankAccount("Ravi", 5000)
    acc.deposit(2000)
    acc.withdraw(1500)
    acc.statement()

    print("\n[2] Student")
    s = Student("Priya", [88, 92, 76, 95, 84])
    s.report()

    print("\n[3] Stack")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())

    print("\n[4] Queue")
    q = Queue()
    q.enqueue("Alice")
    q.enqueue("Bob")
    q.enqueue("Charlie")
    print(q)
    print("Dequeue:", q.dequeue())
    print(q)
