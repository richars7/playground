"""
LeetCode #15: 3Sum
Difficulty: Medium
Key Pattern: Two Pointers + Sorting
Time: O(n²), Space: O(1)

PROBLEM:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

HOW TO THINK:
1. Brute Force: Check all triplets - O(n³) time
2. Sort array first, then for each element, find two others that sum to -element
3. Use two pointers on the remaining array

THINKING STEPS:
1. Sort the array
2. For each element at index i:
   - Skip duplicates for the first element
   - Use two pointers (left = i+1, right = n-1)
   - Find two numbers that sum to -nums[i]
   - Skip duplicates for left and right pointers

HINTS:
- Sort the array first
- For each element, treat it as the first element of triplet
- Use two pointers on the remaining array
- Skip duplicates to avoid duplicate triplets
- When sum equals target, add to result and skip duplicates

EDGE CASES:
- Array with less than 3 elements
- All zeros
- No valid triplets
- Duplicate elements
- All positive or all negative numbers
"""

def threeSum(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {threeSum(nums1)}")  # Expected: [[-1,-1,2],[-1,0,1]]
    
    # Test case 2
    nums2 = [0, 1, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {threeSum(nums2)}")  # Expected: []
    
    # Test case 3
    nums3 = [0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {threeSum(nums3)}")  # Expected: [[0,0,0]]
