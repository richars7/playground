"""
LeetCode #70: Climbing Stairs
Difficulty: Easy
Key Pattern: Fibonacci Sequence
Time: O(n), Space: O(1)

PROBLEM:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

HOW TO THINK:
1. This is essentially the Fibonacci sequence
2. To reach step n, you can come from step n-1 (1 step) or step n-2 (2 steps)
3. So ways(n) = ways(n-1) + ways(n-2)
4. Base cases: ways(1) = 1, ways(2) = 2

THINKING STEPS:
1. Identify the pattern: f(n) = f(n-1) + f(n-2)
2. Set base cases: f(1) = 1, f(2) = 2
3. Build up from base cases to n
4. Can optimize space by only keeping last two values

HINTS:
- This is the Fibonacci sequence
- Use dynamic programming to avoid recalculating
- Can optimize space to O(1) by only keeping last two values
- Base cases: 1 step = 1 way, 2 steps = 2 ways

EDGE CASES:
- n = 1 (1 way)
- n = 2 (2 ways)
- n = 0 (edge case, usually 1 way)
- Large n (watch for integer overflow)
"""

def climbStairs(n):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    print(f"Input: n = {n1}")
    print(f"Output: {climbStairs(n1)}")  # Expected: 3
    
    # Test case 2
    n2 = 2
    print(f"Input: n = {n2}")
    print(f"Output: {climbStairs(n2)}")  # Expected: 2
    
    # Test case 3
    n3 = 1
    print(f"Input: n = {n3}")
    print(f"Output: {climbStairs(n3)}")  # Expected: 1
    
    # Test case 4
    n4 = 5
    print(f"Input: n = {n4}")
    print(f"Output: {climbStairs(n4)}")  # Expected: 8
