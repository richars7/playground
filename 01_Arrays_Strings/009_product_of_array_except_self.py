"""
LeetCode #238: Product of Array Except Self
Difficulty: Medium
Key Pattern: Prefix/Suffix Arrays
Time: O(n), Space: O(1) excluding output array

PROBLEM:
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operator.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: [24,12,8,6] = [2*3*4, 1*3*4, 1*2*4, 1*2*3]

HOW TO THINK:
1. Brute Force: For each element, multiply all others - O(n²) time
2. Use division: Calculate total product, divide by each element - but division not allowed
3. Two-pass approach: Calculate left products, then right products

THINKING STEPS:
1. First pass: Calculate product of all elements to the left of each position
2. Second pass: Calculate product of all elements to the right of each position
3. Combine left and right products for final result
4. Can optimize space by using output array for left products

HINTS:
- Use the result array to store left products first
- Then use a variable to track right product
- For each position i: result[i] = left_product[i] * right_product[i]
- Be careful with the order of operations in the second pass

EDGE CASES:
- Array with zeros
- Array with negative numbers
- Single element array
- Array with all same numbers
- Large numbers (overflow)
"""

def productExceptSelf(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {productExceptSelf(nums1)}")  # Expected: [24,12,8,6]
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {productExceptSelf(nums2)}")  # Expected: [0,0,9,0,0]
    
    # Test case 3
    nums3 = [2, 3, 4, 5]
    print(f"Input: nums = {nums3}")
    print(f"Output: {productExceptSelf(nums3)}")  # Expected: [60,40,30,24]
