"""
LeetCode #55: Jump Game
Difficulty: Medium
Key Pattern: Greedy Algorithm
Time: O(n), Space: O(1)

PROBLEM:
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

HOW TO THINK:
1. Track the furthest index we can reach from current position
2. For each position, update the maximum reachable index
3. If we can reach the last index, return true

THINKING STEPS:
1. Initialize max_reach = 0
2. For each index i:
   - If i > max_reach, we can't reach this position, return false
   - Update max_reach = max(max_reach, i + nums[i])
3. If max_reach >= last_index, return true

HINTS:
- Use greedy approach: track the furthest reachable index
- At each step, check if current index is reachable
- Update the maximum reachable index
- If we can reach the last index, return true

EDGE CASES:
- Single element array
- Array with zeros
- Array where we can't reach the end
- Array where we can reach the end in one jump
"""

def canJump(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [2,3,1,1,4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {canJump(nums1)}")  # Expected: True
    
    # Test case 2
    nums2 = [3,2,1,0,4]
    print(f"Input: nums = {nums2}")
    print(f"Output: {canJump(nums2)}")  # Expected: False
    
    # Test case 3
    nums3 = [0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {canJump(nums3)}")  # Expected: True
