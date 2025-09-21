"""
LeetCode #20: Valid Parentheses
Difficulty: Easy
Key Pattern: Stack for Matching
Time: O(n), Space: O(n)

PROBLEM:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example:
Input: s = "()"
Output: true

HOW TO THINK:
1. This is a classic stack problem
2. When I see an opening bracket, I need to remember it
3. When I see a closing bracket, I need to check if it matches the most recent opening bracket
4. Stack is perfect for "last in, first out" - most recent opening bracket

THINKING STEPS:
1. Use a stack to keep track of opening brackets
2. For each character:
   - If it's an opening bracket, push to stack
   - If it's a closing bracket:
     - Check if stack is empty (no matching opening)
     - Check if it matches the top of stack
     - If matches, pop from stack; if not, return False
3. At the end, stack should be empty (all brackets matched)

HINTS:
- Create a mapping: {')': '(', '}': '{', ']': '['}
- Use a list as a stack
- For closing brackets, check if stack is empty or top doesn't match
- Don't forget to check if stack is empty at the end

EDGE CASES:
- Empty string
- Only opening brackets
- Only closing brackets
- Mismatched brackets
- Nested valid brackets
"""

def isValid(s):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print(f"Input: s = '{s1}'")
    print(f"Output: {isValid(s1)}")  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: s = '{s2}'")
    print(f"Output: {isValid(s2)}")  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print(f"Input: s = '{s3}'")
    print(f"Output: {isValid(s3)}")  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print(f"Input: s = '{s4}'")
    print(f"Output: {isValid(s4)}")  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print(f"Input: s = '{s5}'")
    print(f"Output: {isValid(s5)}")  # Expected: True
