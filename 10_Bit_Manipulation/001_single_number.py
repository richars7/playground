"""
LeetCode #136: Single Number
Difficulty: Easy
Key Pattern: XOR Operation
Time: O(n), Space: O(1)

PROBLEM:
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [2,2,1]
Output: 1

HOW TO THINK:
1. Use XOR operation: a ^ a = 0, a ^ 0 = a
2. XOR all numbers together
3. Numbers appearing twice will cancel out, leaving the single number

THINKING STEPS:
1. Initialize result = 0
2. XOR all numbers in the array
3. Return the result

HINTS:
- Use XOR operation
- XOR has properties: a ^ a = 0, a ^ 0 = a
- XOR is commutative and associative
- All duplicate numbers will cancel out

EDGE CASES:
- Single element array
- All elements the same except one
- Large numbers
- Negative numbers
"""

def singleNumber(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 2, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {singleNumber(nums1)}")  # Expected: 1
    
    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Input: nums = {nums2}")
    print(f"Output: {singleNumber(nums2)}")  # Expected: 4
    
    # Test case 3
    nums3 = [1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {singleNumber(nums3)}")  # Expected: 1
