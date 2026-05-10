"""
=====================================
  TOPIC 1 — STRING MANIPULATION
=====================================
Problems:
  1. Check Palindrome
  2. Count Vowels & Consonants
  3. Caesar Cipher (Encrypt/Decrypt)
  4. Anagram Check
  5. Reverse Words in a Sentence
=====================================
"""

from collections import Counter


# ─────────────────────────────────────
# PROBLEM 1: Check Palindrome
# ─────────────────────────────────────
# A palindrome reads the same forward and backward.
# Example: "racecar", "madam", "A man a plan a canal Panama"

def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# ─────────────────────────────────────
# PROBLEM 2: Count Vowels & Consonants
# ─────────────────────────────────────

def count_vowels_consonants(s: str) -> dict:
    vowels = set("aeiouAEIOU")
    result = {"vowels": 0, "consonants": 0}
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                result["vowels"] += 1
            else:
                result["consonants"] += 1
    return result


# ─────────────────────────────────────
# PROBLEM 3: Caesar Cipher
# ─────────────────────────────────────
# Shift each letter by `shift` positions in the alphabet.
# Example: "abc" with shift=3 → "def"

def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


# ─────────────────────────────────────
# PROBLEM 4: Anagram Check
# ─────────────────────────────────────
# Two strings are anagrams if they have the same characters.
# Example: "listen" and "silent"

def anagram_check(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower())


# ─────────────────────────────────────
# PROBLEM 5: Reverse Words in a Sentence
# ─────────────────────────────────────
# Example: "Hello World" → "World Hello"

def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])


# ─────────────────────────────────────
# RUN & SEE OUTPUT
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 40)
    print("  TOPIC 1 — STRING MANIPULATION")
    print("=" * 40)

    print("\n[1] Palindrome Check")
    print(is_palindrome("racecar"))                        # True
    print(is_palindrome("A man a plan a canal Panama"))    # True
    print(is_palindrome("hello"))                          # False

    print("\n[2] Vowels & Consonants")
    print(count_vowels_consonants("Hello World"))          # vowels:3, consonants:7

    print("\n[3] Caesar Cipher")
    encrypted = caesar_cipher("Hello World", 3)
    print("Encrypted:", encrypted)                         # Khoor Zruog
    print("Decrypted:", caesar_cipher(encrypted, -3))      # Hello World

    print("\n[4] Anagram Check")
    print(anagram_check("listen", "silent"))               # True
    print(anagram_check("hello", "world"))                 # False

    print("\n[5] Reverse Words")
    print(reverse_words("I love Python"))                  # Python love I
