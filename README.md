# DSA: Logic Building Primer

A 4-day, 25-problem primer designed to bridge the gap between Python fundamentals and high-level Data Structures and Algorithms (DSA). This set eliminates redundant basic-math exercises and focuses exclusively on the algorithmic primitives required for Tier-1 tech interviews: pointer manipulation, array invariants, state tracking, and call-stack visualization.

## Core Constraints
To simulate interview conditions and build actual problem-solving logic:
1. **No Typecasting:** Do not convert integers to strings to solve digit or palindrome problems. Use modulo (`%`) and floor division (`//`).
2. **Space Optimization:** For array problems, prioritize in-place modifications ($O(1)$ auxiliary space) unless specifically noted.
3. **No External Libraries:** Build frequency maps and mathematical functions manually.
4. **Target Complexity:** Always analyze and write down the Big-O Time and Space complexity for every solution.

## Progress Tracker

### Category 1: Digit Manipulation & Math Logic
*Goal: Master integer arithmetic and state handling.*
- [ ] 1. Reverse an Integer (Handle 32-bit bounds/negatives)
- [ ] 2. Palindrome Number (Math only, no strings)
- [ ] 3. Count Digits & Digit Sum (Iterative)
- [ ] 4. Greatest Common Divisor (Euclid’s Algorithm - Iterative & Recursive)
- [ ] 5. Fast Exponentiation ($O(\log n)$ time)

### Category 2: Array Invariant & Pointer Logic
*Goal: Master in-place swaps, boundaries, and two-pointer mechanics.*
- [ ] 6. Find Second Largest Element ($O(N)$ time, $O(1)$ space)
- [ ] 7. Check if Array is Sorted and Rotated
- [ ] 8. Remove Duplicates from Sorted Array (In-place, return new length)
- [ ] 9. Move Zeroes (In-place, maintain relative order)
- [ ] 10. Reverse an Array / Subarray In-Place
- [ ] 11. Rotate Array by $K$ Positions ($O(1)$ space reversal algorithm)

### Category 3: Frequency & Hashing Logic
*Goal: Eliminate $O(N^2)$ nested loops using state tracking.*
- [ ] 12. Count Frequencies of Elements (Manual dictionary implementation)
- [ ] 13. Find the Majority Element (Boyer-Moore Voting Algorithm)
- [ ] 14. Find the Single Missing Number (Gauss sum and XOR approaches)
- [ ] 15. Find All Duplicates in an Array ($O(1)$ space, elements $\in [1, n]$)
- [ ] 16. Valid Anagram (Fixed-size frequency array)

### Category 4: String Logic & Index Arithmetic
*Goal: Handle boundary conditions, ASCII parsing, and character pointers.*
- [ ] 17. Valid Palindrome (Alphanumeric only, ignore case, $O(1)$ space)
- [ ] 18. String to Integer (atoi) (Handle leading spaces, signs, and bounds)
- [ ] 19. Longest Common Prefix
- [ ] 20. Reverse Words in a String (Normalize multiple spaces)

### Category 5: Basic Recursion & Call-Stack
*Goal: Establish base cases and trace execution trees.*
- [ ] 21. Factorial & Fibonacci Tracing (Write function + manual stack trace diagram)
- [ ] 22. Recursive Array Sum & Max (Divide and conquer)
- [ ] 23. Recursive String Reversal (Two-index tracking in-place)
- [ ] 24. Check Palindrome Recursively
- [ ] 25. Generate Subsets (Basic backtracking power set)

## Execution Plan

| Day | Focus Area | Problems | Primary Objective |
| :--- | :--- | :--- | :--- |
| **Day 1** | Digit Logic & Basic Math | 1 – 5 | Isolate math logic from string methods. |
| **Day 2** | Array Invariants & Pointers | 6 – 11 | Implement flawless `while` loops with `left`/`right` pointers. |
| **Day 3** | Frequency & Strings | 12 – 20 | Trade memory for time ($O(N)$ hash lookups). |
| **Day 4** | Recursion Call Stack | 21 – 25 | Map the recursive tree to avoid infinite loops and stack overflows. |

## Next Steps
Upon completing this repository, transition immediately to standard pattern-based DSA topics:
1. Sliding Window
2. Two Pointers (Advanced)
3. Binary Search
4. Prefix Sums
5. Linked Lists
