"""
=====================================
  TOPIC 8 — FILE HANDLING
=====================================
Problems:
  1. Write and Read a text file
  2. Append to a file
  3. Count word frequency in a file
  4. Copy one file to another
  5. Read a CSV file manually
=====================================
"""

import os
from collections import Counter


# ─────────────────────────────────────
# PROBLEM 1: Write and Read
# ─────────────────────────────────────

def write_file(filepath: str, content: str) -> None:
    """Overwrite a file with content."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def read_file(filepath: str) -> str:
    """Read and return the full content of a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


# ─────────────────────────────────────
# PROBLEM 2: Append to File
# ─────────────────────────────────────

def append_to_file(filepath: str, content: str) -> None:
    """Add content to end of file without erasing existing content."""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content + "\n")


# ─────────────────────────────────────
# PROBLEM 3: Word Frequency
# ─────────────────────────────────────

def word_frequency(filepath: str) -> dict:
    """Count how often each word appears in a file."""
    with open(filepath, "r", encoding="utf-8") as f:
        words = f.read().lower().split()
    # Remove punctuation from words
    cleaned = [w.strip(".,!?;:\"'()") for w in words]
    return dict(Counter(cleaned).most_common())


# ─────────────────────────────────────
# PROBLEM 4: Copy File
# ─────────────────────────────────────

def copy_file(source: str, destination: str) -> None:
    """Copy contents of source file to destination."""
    with open(source, "r", encoding="utf-8") as src:
        content = src.read()
    with open(destination, "w", encoding="utf-8") as dst:
        dst.write(content)


# ─────────────────────────────────────
# PROBLEM 5: Read CSV Manually
# ─────────────────────────────────────

def read_csv(filepath: str) -> list:
    """Read a CSV file and return list of dicts."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        rows.append(dict(zip(headers, values)))
    return rows


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 8 — FILE HANDLING")
    print("=" * 40)

    # ── Setup temp files ──
    TXT = "sample.txt"
    COPY = "sample_copy.txt"
    CSV = "students.csv"

    # [1] Write and Read
    print("\n[1] Write & Read")
    write_file(TXT, "Python is great.\nFile handling is important.\nPython makes it easy.")
    print(read_file(TXT))

    # [2] Append
    print("\n[2] Append")
    append_to_file(TXT, "This line was appended.")
    print(read_file(TXT))

    # [3] Word Frequency
    print("\n[3] Word Frequency")
    freq = word_frequency(TXT)
    for word, count in list(freq.items())[:5]:
        print(f"  '{word}' → {count}")

    # [4] Copy File
    print("\n[4] Copy File")
    copy_file(TXT, COPY)
    print(f"Copied to '{COPY}'. Contents match: {read_file(TXT) == read_file(COPY)}")

    # [5] CSV
    print("\n[5] Read CSV")
    write_file(CSV, "name,age,grade\nAlice,17,A\nBob,16,B\nPriya,17,A+")
    students = read_csv(CSV)
    for s in students:
        print(f"  {s}")

    # ── Cleanup ──
    for f in [TXT, COPY, CSV]:
        if os.path.exists(f):
            os.remove(f)
