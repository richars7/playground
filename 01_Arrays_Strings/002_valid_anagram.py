"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Key Pattern: Character Frequency Counting
Time: O(n), Space: O(1) - since we only have 26 lowercase letters

PROBLEM:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

HOW TO THINK:
1. What makes two strings anagrams? Same characters, same frequencies
2. If lengths are different, they can't be anagrams
3. Count character frequencies in both strings
4. Compare the counts

THINKING STEPS:
1. Check if lengths are equal - if not, return False
2. Count characters in first string
3. For each character in second string, decrease count
4. If any count becomes negative or remains positive, not anagram

HINTS:
- Use a dictionary to count characters
- For lowercase letters only, you can use an array of size 26
- ord('a') gives ASCII value of 'a'
- ord(char) - ord('a') gives index 0-25 for lowercase letters

EDGE CASES:
- Different lengths
- Empty strings
- Single character strings
- Strings with repeated characters
"""

def isAnagram(s, t):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    s1, t1 = "anagram", "nagaram"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Output: {isAnagram(s1, t1)}")  # Expected: True
    
    # Test case 2
    s2, t2 = "rat", "car"
    print(f"Input: s = '{s2}', t = '{t2}'")
    print(f"Output: {isAnagram(s2, t2)}")  # Expected: False
    
    # Test case 3
    s3, t3 = "a", "ab"
    print(f"Input: s = '{s3}', t = '{t3}'")
    print(f"Output: {isAnagram(s3, t3)}")  # Expected: False
