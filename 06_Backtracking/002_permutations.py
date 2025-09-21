"""
LeetCode #46: Permutations
Difficulty: Medium
Key Pattern: Backtracking with Visited Array
Time: O(n!), Space: O(n!)

PROBLEM:
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

HOW TO THINK:
1. Use backtracking to generate all permutations
2. For each position, try all unused numbers
3. Use a visited array to track which numbers are used

THINKING STEPS:
1. Use backtracking with a current permutation and visited array
2. For each recursive call:
   - Try each unused number
   - Add it to current permutation
   - Mark as visited
   - Recurse
   - Backtrack (remove from permutation, mark as unvisited)
3. When permutation is complete, add to result

HINTS:
- Use backtracking with visited array
- For each position, try all unused numbers
- Mark numbers as visited/unvisited during recursion
- Add complete permutations to result

EDGE CASES:
- Single element array
- Two elements
- Empty array
- All elements the same (but problem says distinct)
"""

def permute(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Input: nums = {nums1}")
    result1 = permute(nums1)
    print(f"Output: {result1}")  # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    
    # Test case 2
    nums2 = [0, 1]
    print(f"Input: nums = {nums2}")
    result2 = permute(nums2)
    print(f"Output: {result2}")  # Expected: [[0,1],[1,0]]
    
    # Test case 3
    nums3 = [1]
    print(f"Input: nums = {nums3}")
    result3 = permute(nums3)
    print(f"Output: {result3}")  # Expected: [[1]]
