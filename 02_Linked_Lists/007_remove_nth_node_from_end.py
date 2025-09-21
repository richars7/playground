"""
LeetCode #19: Remove Nth Node From End of List
Difficulty: Medium
Key Pattern: Two Pointers with Gap
Time: O(n), Space: O(1)

PROBLEM:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

HOW TO THINK:
1. Use two pointers with a gap of n between them
2. Move both pointers until the first pointer reaches the end
3. The second pointer will be at the node before the one to remove

THINKING STEPS:
1. Create dummy node to handle edge case (removing head)
2. Move first pointer n steps ahead
3. Move both pointers until first pointer reaches end
4. Remove the nth node by updating pointers
5. Return dummy.next

HINTS:
- Use dummy node to handle removing the head
- Create gap of n between two pointers
- Move both pointers until first reaches end
- Second pointer will be at node before target

EDGE CASES:
- Removing the head node
- Single node list
- n equals length of list
- n = 1 (removing last node)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
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
    n1 = 2
    print(f"Input: head = {linkedListToArray(head1)}, n = {n1}")
    result1 = removeNthFromEnd(head1, n1)
    print(f"Output: {linkedListToArray(result1)}")  # Expected: [1,2,3,5]
    
    # Test case 2
    head2 = createLinkedList([1])
    n2 = 1
    print(f"Input: head = {linkedListToArray(head2)}, n = {n2}")
    result2 = removeNthFromEnd(head2, n2)
    print(f"Output: {linkedListToArray(result2)}")  # Expected: []
    
    # Test case 3
    head3 = createLinkedList([1, 2])
    n3 = 1
    print(f"Input: head = {linkedListToArray(head3)}, n = {n3}")
    result3 = removeNthFromEnd(head3, n3)
    print(f"Output: {linkedListToArray(result3)}")  # Expected: [1]
