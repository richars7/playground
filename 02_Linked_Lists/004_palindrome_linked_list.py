"""
LeetCode #234: Palindrome Linked List
Difficulty: Easy
Key Pattern: Reverse Half + Two Pointers
Time: O(n), Space: O(1)

PROBLEM:
Given the head of a singly linked list, return true if it is a palindrome.

Example:
Input: head = [1,2,2,1]
Output: true

HOW TO THINK:
1. Find the middle of the list
2. Reverse the second half
3. Compare first half with reversed second half
4. Restore the list (optional)

THINKING STEPS:
1. Use slow/fast pointers to find middle
2. Reverse the second half of the list
3. Compare first half with reversed second half
4. Return True if all values match

HINTS:
- Use slow/fast pointers to find middle
- Reverse the second half of the list
- Compare values from both halves
- Don't forget to handle odd/even length lists

EDGE CASES:
- Empty list
- Single node
- Two nodes (same/different values)
- Odd/even length lists
- Already palindrome
- Not a palindrome
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # TODO: Implement your solution here
    pass

# Helper function to create linked list from array
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# Test your solution
if __name__ == "__main__":
    # Test case 1
    head1 = createLinkedList([1, 2, 2, 1])
    print(f"Input: {[1, 2, 2, 1]}")
    print(f"Output: {isPalindrome(head1)}")  # Expected: True
    
    # Test case 2
    head2 = createLinkedList([1, 2])
    print(f"Input: {[1, 2]}")
    print(f"Output: {isPalindrome(head2)}")  # Expected: False
    
    # Test case 3
    head3 = createLinkedList([1, 2, 3, 2, 1])
    print(f"Input: {[1, 2, 3, 2, 1]}")
    print(f"Output: {isPalindrome(head3)}")  # Expected: True
