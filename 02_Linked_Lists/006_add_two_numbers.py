"""
LeetCode #2: Add Two Numbers
Difficulty: Medium
Key Pattern: Digit-by-Digit Addition + Carry
Time: O(max(m,n)), Space: O(max(m,n))

PROBLEM:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

HOW TO THINK:
1. Add digits from both lists starting from the head
2. Handle carry when sum >= 10
3. Create new nodes for the result
4. Handle different lengths of lists

THINKING STEPS:
1. Initialize dummy node and current pointer
2. While either list has nodes or carry exists:
   - Get values from both lists (0 if None)
   - Calculate sum and carry
   - Create new node with sum % 10
   - Move pointers
3. Return dummy.next

HINTS:
- Use dummy node to simplify edge cases
- Handle carry properly
- When one list is shorter, treat missing digits as 0
- Don't forget to handle final carry

EDGE CASES:
- Lists of different lengths
- Final carry (e.g., 5 + 5 = 10)
- One list is empty
- Both lists are empty
- Large numbers
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
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
    l1 = createLinkedList([2, 4, 3])
    l2 = createLinkedList([5, 6, 4])
    print(f"Input: l1 = {linkedListToArray(l1)}, l2 = {linkedListToArray(l2)}")
    result = addTwoNumbers(l1, l2)
    print(f"Output: {linkedListToArray(result)}")  # Expected: [7,0,8]
    
    # Test case 2
    l3 = createLinkedList([0])
    l4 = createLinkedList([0])
    print(f"Input: l1 = {linkedListToArray(l3)}, l2 = {linkedListToArray(l4)}")
    result2 = addTwoNumbers(l3, l4)
    print(f"Output: {linkedListToArray(result2)}")  # Expected: [0]
    
    # Test case 3
    l5 = createLinkedList([9, 9, 9, 9, 9, 9, 9])
    l6 = createLinkedList([9, 9, 9, 9])
    print(f"Input: l1 = {linkedListToArray(l5)}, l2 = {linkedListToArray(l6)}")
    result3 = addTwoNumbers(l5, l6)
    print(f"Output: {linkedListToArray(result3)}")  # Expected: [8,9,9,9,0,0,0,1]
