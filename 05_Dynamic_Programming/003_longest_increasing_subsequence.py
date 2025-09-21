"""
LeetCode #300: Longest Increasing Subsequence
Difficulty: Medium
Key Pattern: Dynamic Programming + Binary Search
Time: O(n log n), Space: O(n)

PROBLEM:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,18], therefore the length is 4.

HOW TO THINK:
1. Brute Force: Check all subsequences - O(2^n) time
2. DP: For each element, find longest subsequence ending at that element
3. Optimized: Use binary search to maintain a sorted array of smallest tail elements

THINKING STEPS:
1. Create array to store smallest tail element for each length
2. For each number, use binary search to find position
3. If number is larger than all tails, extend array
4. Otherwise, replace first element >= number

HINTS:
- Use binary search to maintain sorted array of tails
- For each number, find where it should be placed
- If it's larger than all, extend the array
- Otherwise, replace the first element >= current number

EDGE CASES:
- Empty array
- Single element
- Decreasing array
- Increasing array
- Duplicate elements
"""

def lengthOfLIS(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [10,9,2,5,3,7,101,18]
    print(f"Input: nums = {nums1}")
    print(f"Output: {lengthOfLIS(nums1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [0,1,0,3,2,3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {lengthOfLIS(nums2)}")  # Expected: 4
    
    # Test case 3
    nums3 = [7,7,7,7,7,7,7]
    print(f"Input: nums = {nums3}")
    print(f"Output: {lengthOfLIS(nums3)}")  # Expected: 1
