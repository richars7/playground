"""
LeetCode #189: Rotate Array
Difficulty: Medium
Key Pattern: Array Reversal
Time: O(n), Space: O(1)

PROBLEM:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

HOW TO THINK:
1. Brute Force: Rotate one step at a time - O(n*k) time
2. Extra Array: Copy elements to new positions - O(n) time, O(n) space
3. Array Reversal: Reverse entire array, then reverse first k and last n-k elements

THINKING STEPS:
1. Handle edge case: k might be larger than array length
2. Reverse the entire array
3. Reverse the first k elements
4. Reverse the remaining elements

HINTS:
- Use array reversal technique for O(1) space
- First reverse entire array
- Then reverse first k elements
- Finally reverse remaining elements
- Handle k > n by using k % n

EDGE CASES:
- k = 0 (no rotation needed)
- k = n (full rotation, back to original)
- k > n (use modulo)
- Single element array
- Empty array
"""

def rotate(nums, k):
    # TODO: Implement your solution here
    # Note: Modify nums in-place and return it
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    print(f"Input: nums = {nums1}, k = {k1}")
    rotate(nums1, k1)
    print(f"Output: {nums1}")  # Expected: [5,6,7,1,2,3,4]
    
    # Test case 2
    nums2 = [-1,-100,3,99]
    k2 = 2
    print(f"Input: nums = {nums2}, k = {k2}")
    rotate(nums2, k2)
    print(f"Output: {nums2}")  # Expected: [3,99,-1,-100]
    
    # Test case 3
    nums3 = [1,2]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    rotate(nums3, k3)
    print(f"Output: {nums3}")  # Expected: [2,1]
