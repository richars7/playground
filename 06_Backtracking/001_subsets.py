"""
LeetCode #78: Subsets
Difficulty: Medium
Key Pattern: Decision Tree (Include/Exclude)
Time: O(2^n), Space: O(2^n)

PROBLEM:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

HOW TO THINK:
1. For each element, I have two choices: include it or exclude it
2. This creates a binary decision tree
3. Use backtracking to explore all possibilities
4. Add current subset to result at each step

THINKING STEPS:
1. Start with empty subset
2. For each element, make two recursive calls:
   - One including the current element
   - One excluding the current element
3. Add current subset to result
4. Backtrack by removing the last added element

HINTS:
- Use backtracking with recursion
- For each element, decide to include or exclude
- Add current subset to result at each recursive call
- Backtrack by removing the last element
- Start with empty subset

EDGE CASES:
- Empty array
- Single element array
- Two elements
- All elements the same (but problem says unique elements)
"""

def subsets(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Input: nums = {nums1}")
    result1 = subsets(nums1)
    print(f"Output: {result1}")  # Expected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    
    # Test case 2
    nums2 = [0]
    print(f"Input: nums = {nums2}")
    result2 = subsets(nums2)
    print(f"Output: {result2}")  # Expected: [[],[0]]
    
    # Test case 3
    nums3 = [1, 2]
    print(f"Input: nums = {nums3}")
    result3 = subsets(nums3)
    print(f"Output: {result3}")  # Expected: [[],[1],[2],[1,2]]
