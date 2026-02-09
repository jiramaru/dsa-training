# Exercise 1 - Programming Problems (Logic & Algorithms)

## Problem 1: Divisible Numbers (Easy)

**Objective:** Iterate through numbers from 1 to N and display a value based on divisors.

**Input:** N A B word1 word2 (example: 10 2 3 pair triple)
- N: the maximum number (inclusive)
- A: first divisor
- B: second divisor
- word1: text to display if divisible by A
- word2: text to display if divisible by B

**Output:** For each number from 1 to N:
- If divisible by A and B: display word1+word2
- If divisible by A only: display word1
- If divisible by B only: display word2
- Otherwise: display the number

**Examples:**
```
Input: 10 2 3 pair triple
Output: 1 pair triple pair 5 pair triple pair 9 pair triple

Input: 10 3 5 trip cinquo
Output: 1 2 trip 4 cinquo trip 7 8 trip cinquo
```

---

## Problem 2: Palindrome Checker (Easy)

**Objective:** Check if a line of text is a palindrome (reads identically in both directions).

**Rules:**
- Ignore spaces and punctuation
- Ignore case (uppercase/lowercase)
- Consider only letters and digits

**Input:** A line of text (UTF-8)

**Output:** YES (if palindrome) or NO (if not palindrome)

**Example:**
```
Input: "Esope reste ici et se repose"
Output: YES
```

---

## Problem 3: Most Frequent Element (Easy to Medium)

**Objective:** Find the element that appears most often in a list and count how many times.

**Input:** First number n (number of elements), followed by n elements
- Elements can be numbers or text
- n can be 0 (empty list)

**Output:** Two values: element frequency
- If multiple elements have the same maximum frequency, return the first encountered
- If the list is empty, display: "empty 0"

**Example:**
```
Input: 5 chat chien chat oiseau chat
Output: chat 3
(Explanation: "chat" appears 3 times, it's the most frequent)
```

---

## Submission Instructions
- Create your solutions in a folder: solutions/\<your_name\>
- Handle edge cases (empty input, ties, etc.)
- Respect the exact input/output format requested
