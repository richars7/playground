"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Key Pattern: Hash Map + Sorting
Time: O(n*k*log(k)), Space: O(n*k)

PROBLEM:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

HOW TO THINK:
1. Anagrams have the same characters when sorted
2. Use sorted string as key in hash map
3. Group strings with same sorted key together

THINKING STEPS:
1. For each string, sort its characters to get a key
2. Use this key to group anagrams in a hash map
3. Return all groups as a list of lists

HINTS:
- Sort each string to create a unique key for anagrams
- Use a dictionary where key is sorted string, value is list of anagrams
- Alternative: Use character frequency count as key
- Don't forget to convert sorted result back to string

EDGE CASES:
- Empty array
- Single string
- All strings are anagrams
- No anagrams (all unique)
- Empty strings
"""

def groupAnagrams(strs):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    print(f"Input: strs = {strs1}")
    print(f"Output: {groupAnagrams(strs1)}")  # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    # Test case 2
    strs2 = [""]
    print(f"Input: strs = {strs2}")
    print(f"Output: {groupAnagrams(strs2)}")  # Expected: [[""]]
    
    # Test case 3
    strs3 = ["a"]
    print(f"Input: strs = {strs3}")
    print(f"Output: {groupAnagrams(strs3)}")  # Expected: [["a"]]
