"""
LeetCode #1: Two Sum
Difficulty: Easy
Key Pattern: Hash Map
Time: O(n), Space: O(n)

PROBLEM:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

HOW TO THINK:
1. Brute Force: Check every pair - O(n²) time
2. Hash Map: For each number, check if (target - number) exists in map
3. Key insight: Store numbers as you go, check complements

THINKING STEPS:
1. What if I use a hash map to store numbers I've seen?
2. For each number, what's its complement (target - current_number)?
3. If complement exists in map, I found the pair!
4. Otherwise, add current number to map and continue

HINTS:
- Use a dictionary to store {number: index}
- For each number, calculate complement = target - number
- If complement in dictionary, return [dict[complement], current_index]
- Otherwise, add current number to dictionary

EDGE CASES:
- Empty array
- No solution (but problem guarantees one exists)
- Duplicate numbers
"""

def twoSum(nums, target):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {twoSum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {twoSum(nums3, target3)}")  # Expected: [0, 1]
