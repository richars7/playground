"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Key Pattern: Sliding Window + Hash Set
Time: O(n), Space: O(min(m,n)) where m is charset size

PROBLEM:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

HOW TO THINK:
1. Brute Force: Check all substrings - O(n³) time
2. Sliding Window: Use two pointers to maintain a window of unique characters
3. When we find a duplicate, shrink the window from the left

THINKING STEPS:
1. Use two pointers: left and right
2. Use a set to track characters in current window
3. Move right pointer, add characters to set
4. If we find a duplicate, move left pointer until no duplicates
5. Keep track of maximum window size

HINTS:
- Use a set to store characters in current window
- When right pointer finds a duplicate, move left pointer
- Remove characters from set as left pointer moves
- Update maximum length when window is valid
- Alternative: Use hash map to store character indices for faster left pointer movement

EDGE CASES:
- Empty string
- Single character string
- All characters the same
- No repeating characters
- String with spaces or special characters
"""

def lengthOfLongestSubstring(s):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: s = '{s1}'")
    print(f"Output: {lengthOfLongestSubstring(s1)}")  # Expected: 3
    
    # Test case 2
    s2 = "bbbbb"
    print(f"Input: s = '{s2}'")
    print(f"Output: {lengthOfLongestSubstring(s2)}")  # Expected: 1
    
    # Test case 3
    s3 = "pwwkew"
    print(f"Input: s = '{s3}'")
    print(f"Output: {lengthOfLongestSubstring(s3)}")  # Expected: 3
    
    # Test case 4
    s4 = ""
    print(f"Input: s = '{s4}'")
    print(f"Output: {lengthOfLongestSubstring(s4)}")  # Expected: 0
