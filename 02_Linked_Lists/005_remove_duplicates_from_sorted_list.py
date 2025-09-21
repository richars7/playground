"""
LeetCode #83: Remove Duplicates from Sorted List
Difficulty: Easy
Key Pattern: Single Pointer Traversal
Time: O(n), Space: O(1)

PROBLEM:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example:
Input: head = [1,1,2]
Output: [1,2]

HOW TO THINK:
1. Since list is sorted, duplicates will be adjacent
2. For each node, check if next node has same value
3. If yes, skip the next node; if no, move to next node

THINKING STEPS:
1. Start from head
2. For each node, check if next node has same value
3. If duplicate found, skip next node
4. If no duplicate, move to next node
5. Continue until end of list

HINTS:
- Use a single pointer to traverse the list
- Compare current node value with next node value
- If they're equal, skip the next node
- If they're different, move to next node

EDGE CASES:
- Empty list
- Single node
- All nodes are duplicates
- No duplicates
- Duplicates at the end
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
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
    head1 = createLinkedList([1, 1, 2])
    print(f"Input: {[1, 1, 2]}")
    result1 = deleteDuplicates(head1)
    print(f"Output: {linkedListToArray(result1)}")  # Expected: [1, 2]
    
    # Test case 2
    head2 = createLinkedList([1, 1, 2, 3, 3])
    print(f"Input: {[1, 1, 2, 3, 3]}")
    result2 = deleteDuplicates(head2)
    print(f"Output: {linkedListToArray(result2)}")  # Expected: [1, 2, 3]
    
    # Test case 3
    head3 = createLinkedList([1, 1, 1])
    print(f"Input: {[1, 1, 1]}")
    result3 = deleteDuplicates(head3)
    print(f"Output: {linkedListToArray(result3)}")  # Expected: [1]
