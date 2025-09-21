"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Key Pattern: Hash Set
Time: O(n), Space: O(n)

PROBLEM:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

HOW TO THINK:
1. Brute Force: Check every pair - O(n²) time
2. Sort and check adjacent elements - O(n log n) time
3. Use a set to track seen numbers - O(n) time

THINKING STEPS:
1. Keep track of numbers I've seen so far
2. For each number, check if I've seen it before
3. If yes, return True (duplicate found)
4. If no, add it to my "seen" collection and continue
5. If I finish the array without finding duplicates, return False

HINTS:
- Use a set to store seen numbers
- For each number, check if it's in the set
- If found, return True immediately
- If not found, add to set and continue
- Alternative: Compare length of array with length of set

EDGE CASES:
- Empty array
- Single element array
- All elements the same
- Large array with no duplicates
"""

def containsDuplicate(nums):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {containsDuplicate(nums1)}")  # Expected: True
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: nums = {nums2}")
    print(f"Output: {containsDuplicate(nums2)}")  # Expected: False
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {containsDuplicate(nums3)}")  # Expected: True
