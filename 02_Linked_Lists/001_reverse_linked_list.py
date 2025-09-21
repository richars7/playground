"""
LeetCode #206: Reverse Linked List
Difficulty: Easy
Key Pattern: Three Pointers (prev, curr, next)
Time: O(n), Space: O(1)

PROBLEM:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

HOW TO THINK:
1. Need to reverse the direction of all pointers
2. Keep track of previous, current, and next nodes
3. For each node, point it to the previous node

THINKING STEPS:
1. Initialize prev = None, curr = head
2. For each node:
   - Store next node before changing pointer
   - Point current node to previous node
   - Move prev to curr, curr to next
3. Return prev (new head)

HINTS:
- Use three pointers: prev, curr, next
- Always store next before changing curr.next
- The new head will be the last node (prev after loop)
- Handle edge case: empty list or single node

EDGE CASES:
- Empty list (None)
- Single node list
- Two node list
- Already reversed list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
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

# Helper function to convert linked list to array
def linkedListToArray(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Test your solution
if __name__ == "__main__":
    # Test case 1
    head1 = createLinkedList([1, 2, 3, 4, 5])
    print(f"Input: {linkedListToArray(head1)}")
    reversed_head1 = reverseList(head1)
    print(f"Output: {linkedListToArray(reversed_head1)}")  # Expected: [5,4,3,2,1]
    
    # Test case 2
    head2 = createLinkedList([1, 2])
    print(f"Input: {linkedListToArray(head2)}")
    reversed_head2 = reverseList(head2)
    print(f"Output: {linkedListToArray(reversed_head2)}")  # Expected: [2,1]
    
    # Test case 3
    head3 = createLinkedList([])
    print(f"Input: {linkedListToArray(head3)}")
    reversed_head3 = reverseList(head3)
    print(f"Output: {linkedListToArray(reversed_head3)}")  # Expected: []
