"""
LeetCode #11: Container With Most Water
Difficulty: Medium
Key Pattern: Two Pointers
Time: O(n), Space: O(1)

PROBLEM:
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

HOW TO THINK:
1. Brute Force: Check all pairs - O(n²) time
2. Two Pointers: Start from both ends, move inward
3. Key insight: Always move the pointer with the smaller height

THINKING STEPS:
1. Start with left = 0, right = n-1
2. Calculate current area = min(height[left], height[right]) * (right - left)
3. Update maximum area
4. Move the pointer with smaller height inward
5. Why? Moving the larger height pointer can only decrease area

HINTS:
- Use two pointers: left and right
- Calculate area = min(height[left], height[right]) * width
- Move the pointer with smaller height
- Keep track of maximum area seen so far
- The key insight: moving the larger height pointer can't improve the area

EDGE CASES:
- Two elements
- All heights the same
- Increasing heights
- Decreasing heights
- Single peak in the middle
"""

def maxArea(height):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Input: height = {height1}")
    print(f"Output: {maxArea(height1)}")  # Expected: 49
    
    # Test case 2
    height2 = [1, 1]
    print(f"Input: height = {height2}")
    print(f"Output: {maxArea(height2)}")  # Expected: 1
    
    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    print(f"Input: height = {height3}")
    print(f"Output: {maxArea(height3)}")  # Expected: 16
