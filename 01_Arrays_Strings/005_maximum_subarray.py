"""
LeetCode #53: Maximum Subarray
Difficulty: Easy
Key Pattern: Kadane's Algorithm
Time: O(n), Space: O(1)

PROBLEM:
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

HOW TO THINK:
1. Brute Force: Check all possible subarrays - O(n³) time
2. Kadane's Algorithm: Keep track of current sum and maximum sum seen so far
3. Key insight: If current sum becomes negative, it's better to start fresh

THINKING STEPS:
1. Keep track of current sum and maximum sum
2. For each element:
   - Add it to current sum
   - If current sum becomes negative, reset it to 0 (start fresh)
   - Update maximum sum if current sum is greater
3. Return maximum sum

HINTS:
- Initialize max_sum to first element (in case all are negative)
- Initialize current_sum to 0
- For each number: current_sum = max(number, current_sum + number)
- Update max_sum = max(max_sum, current_sum)
- This handles the case where we should start a new subarray

EDGE CASES:
- All negative numbers
- Single element array
- Array with zeros
- Mixed positive and negative numbers
"""

def maxSubArray(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {maxSubArray(nums1)}")  # Expected: 6
    
    # Test case 2
    nums2 = [1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {maxSubArray(nums2)}")  # Expected: 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"Input: nums = {nums3}")
    print(f"Output: {maxSubArray(nums3)}")  # Expected: 23
