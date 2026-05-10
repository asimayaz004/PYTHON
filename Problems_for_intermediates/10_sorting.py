"""
=====================================
  TOPIC 10 — SORTING ALGORITHMS
=====================================
Algorithms:
  1. Bubble Sort
  2. Selection Sort
  3. Insertion Sort
  4. Merge Sort
  5. Quick Sort

Each one includes:
  - Clean implementation
  - Step counter (to compare efficiency)
  - Plain English explanation in comments
=====================================
"""


# ─────────────────────────────────────
# ALGORITHM 1: Bubble Sort
# ─────────────────────────────────────
# Repeatedly swap adjacent elements if they're in the wrong order.
# Like bubbles rising — largest values "bubble" to the end.
# Time complexity: O(n²)

def bubble_sort(arr: list) -> tuple:
    a = arr.copy()
    steps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, steps


# ─────────────────────────────────────
# ALGORITHM 2: Selection Sort
# ─────────────────────────────────────
# Find the minimum element and place it at the start, repeat.
# Like picking the smallest card from your hand each time.
# Time complexity: O(n²)

def selection_sort(arr: list) -> tuple:
    a = arr.copy()
    steps = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, steps


# ─────────────────────────────────────
# ALGORITHM 3: Insertion Sort
# ─────────────────────────────────────
# Pick each element and insert it in the right place in sorted part.
# Like sorting playing cards in your hand one by one.
# Time complexity: O(n²) worst, O(n) best

def insertion_sort(arr: list) -> tuple:
    a = arr.copy()
    steps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            steps += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a, steps


# ─────────────────────────────────────
# ALGORITHM 4: Merge Sort
# ─────────────────────────────────────
# Divide the list in half, sort each half, then merge them.
# Divide and Conquer strategy.
# Time complexity: O(n log n)

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ─────────────────────────────────────
# ALGORITHM 5: Quick Sort
# ─────────────────────────────────────
# Pick a pivot, put smaller elements left, larger right. Repeat.
# Time complexity: O(n log n) average, O(n²) worst

def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 10 — SORTING ALGORITHMS")
    print("=" * 40)

    data = [64, 25, 12, 22, 11, 90, 43, 7, 55, 30]
    print(f"\nOriginal: {data}")

    sorted_b, steps_b = bubble_sort(data)
    sorted_s, steps_s = selection_sort(data)
    sorted_i, steps_i = insertion_sort(data)
    sorted_m          = merge_sort(data)
    sorted_q          = quick_sort(data)

    print(f"\n{'Algorithm':<18} {'Sorted Result':<35} {'Steps':>6}")
    print("-" * 62)
    print(f"{'Bubble Sort':<18} {str(sorted_b):<35} {steps_b:>6}")
    print(f"{'Selection Sort':<18} {str(sorted_s):<35} {steps_s:>6}")
    print(f"{'Insertion Sort':<18} {str(sorted_i):<35} {steps_i:>6}")
    print(f"{'Merge Sort':<18} {str(sorted_m):<35} {'O(nlogn)':>6}")
    print(f"{'Quick Sort':<18} {str(sorted_q):<35} {'O(nlogn)':>6}")

    print("\n📊 Efficiency: Quick/Merge > Insertion > Selection > Bubble")
    print("   For small lists, Insertion Sort is actually fastest in practice.")
