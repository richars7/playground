"""
LeetCode #39: Combination Sum
Difficulty: Medium
Key Pattern: Backtracking with Index
Time: O(2^target), Space: O(target)

PROBLEM:
Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the 
combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

HOW TO THINK:
1. Use backtracking to explore all possible combinations
2. For each number, decide how many times to use it
3. Use index to avoid duplicate combinations

THINKING STEPS:
1. Sort candidates to handle duplicates easily
2. Use backtracking with current combination and remaining target
3. For each candidate starting from current index:
   - If candidate <= remaining target, add it to combination
   - Recurse with same index (can reuse same number)
   - Backtrack by removing the number
4. If target becomes 0, add combination to result

HINTS:
- Use backtracking with index to avoid duplicates
- Sort candidates first
- For each number, try using it multiple times
- Use index to ensure we don't go backwards

EDGE CASES:
- No valid combinations
- Single candidate that equals target
- All candidates larger than target
- Target = 0
"""

def combinationSum(candidates, target):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(f"Input: candidates = {candidates1}, target = {target1}")
    result1 = combinationSum(candidates1, target1)
    print(f"Output: {result1}")  # Expected: [[2,2,3],[7]]
    
    # Test case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    print(f"Input: candidates = {candidates2}, target = {target2}")
    result2 = combinationSum(candidates2, target2)
    print(f"Output: {result2}")  # Expected: [[2,2,2,2],[2,3,3],[3,5]]
    
    # Test case 3
    candidates3 = [2]
    target3 = 1
    print(f"Input: candidates = {candidates3}, target = {target3}")
    result3 = combinationSum(candidates3, target3)
    print(f"Output: {result3}")  # Expected: []
