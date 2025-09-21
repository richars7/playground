"""
LeetCode #69: Sqrt(x)
Difficulty: Easy
Key Pattern: Binary Search
Time: O(log x), Space: O(1)

PROBLEM:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

Example:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

HOW TO THINK:
1. Brute Force: Check each number from 1 to x - O(√x) time
2. Binary Search: Search in range [0, x] - O(log x) time
3. Use binary search to find the largest number whose square <= x

THINKING STEPS:
1. Handle edge cases: x = 0, x = 1
2. Use binary search in range [0, x]
3. For each mid, check if mid^2 <= x
4. If yes, try larger numbers; if no, try smaller numbers
5. Return the largest valid number

HINTS:
- Use binary search to find square root
- Search in range [0, x]
- Check if mid^2 <= x
- Be careful with integer overflow

EDGE CASES:
- x = 0 (return 0)
- x = 1 (return 1)
- Perfect squares
- Large numbers
- Integer overflow
"""

def mySqrt(x):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    x1 = 8
    print(f"Input: x = {x1}")
    print(f"Output: {mySqrt(x1)}")  # Expected: 2
    
    # Test case 2
    x2 = 4
    print(f"Input: x = {x2}")
    print(f"Output: {mySqrt(x2)}")  # Expected: 2
    
    # Test case 3
    x3 = 0
    print(f"Input: x = {x3}")
    print(f"Output: {mySqrt(x3)}")  # Expected: 0
