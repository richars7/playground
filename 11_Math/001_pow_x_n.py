"""
LeetCode #50: Pow(x, n)
Difficulty: Medium
Key Pattern: Divide and Conquer
Time: O(log n), Space: O(log n)

PROBLEM:
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

HOW TO THINK:
1. Brute Force: Multiply x n times - O(n) time
2. Optimized: Use divide and conquer - O(log n) time
3. Handle negative exponents by taking reciprocal

THINKING STEPS:
1. Handle edge cases: n = 0, n = 1, n < 0
2. Use divide and conquer: x^n = x^(n/2) * x^(n/2)
3. If n is odd, multiply by x once more
4. Handle negative n by taking reciprocal

HINTS:
- Use divide and conquer for O(log n) time
- x^n = x^(n/2) * x^(n/2) if n is even
- x^n = x^(n/2) * x^(n/2) * x if n is odd
- Handle negative exponents

EDGE CASES:
- n = 0 (return 1)
- n = 1 (return x)
- n < 0 (return 1/pow(x, -n))
- x = 0
- Very large n
"""

def myPow(x, n):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    x1, n1 = 2.00000, 10
    print(f"Input: x = {x1}, n = {n1}")
    print(f"Output: {myPow(x1, n1)}")  # Expected: 1024.0
    
    # Test case 2
    x2, n2 = 2.10000, 3
    print(f"Input: x = {x2}, n = {n2}")
    print(f"Output: {myPow(x2, n2)}")  # Expected: 9.261
    
    # Test case 3
    x3, n3 = 2.00000, -2
    print(f"Input: x = {x3}, n = {n3}")
    print(f"Output: {myPow(x3, n3)}")  # Expected: 0.25
