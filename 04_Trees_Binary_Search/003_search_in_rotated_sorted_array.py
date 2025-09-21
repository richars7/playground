"""
LeetCode #33: Search in Rotated Sorted Array
Difficulty: Medium
Key Pattern: Modified Binary Search
Time: O(log n), Space: O(1)

PROBLEM:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k.

Given the array nums after the possible rotation and an integer target, return the index of target 
if it is in nums, or -1 if it is not in nums.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

HOW TO THINK:
1. The array is rotated, so we can't use normal binary search
2. Find which half is sorted and check if target is in that range
3. If target is in sorted half, search there; otherwise search other half

THINKING STEPS:
1. Use binary search with modified conditions
2. Check which half is sorted (left or right)
3. If target is in sorted half, search there
4. Otherwise, search in the other half
5. Continue until found or search space is exhausted

HINTS:
- Modified binary search for rotated array
- Check which half is sorted by comparing mid with left/right
- If left half is sorted and target is in range, search left
- If right half is sorted and target is in range, search right
- Otherwise, search the other half

EDGE CASES:
- Target not found
- Target at pivot point
- Array not rotated
- Single element array
- Target at boundaries
"""

def search(nums, target):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {search(nums1, target1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {search(nums2, target2)}")  # Expected: -1
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {search(nums3, target3)}")  # Expected: -1
