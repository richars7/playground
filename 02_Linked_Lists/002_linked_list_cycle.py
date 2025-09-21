"""
LeetCode #141: Linked List Cycle
Difficulty: Easy
Key Pattern: Floyd's Cycle Detection (Slow/Fast Pointers)
Time: O(n), Space: O(1)

PROBLEM:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer.

Example:
Input: head = [3,2,0,-4], pos = 1 (cycle from -4 to 2)
Output: true

HOW TO THINK:
1. If there's a cycle, a fast pointer will eventually catch up to slow pointer
2. Use two pointers: slow (moves 1 step) and fast (moves 2 steps)
3. If they meet, there's a cycle; if fast reaches end, no cycle

THINKING STEPS:
1. Initialize slow = head, fast = head
2. Move slow by 1, fast by 2
3. If fast meets slow, there's a cycle
4. If fast reaches None, no cycle

HINTS:
- Use Floyd's cycle detection algorithm
- Slow pointer moves 1 step, fast pointer moves 2 steps
- Check if fast and fast.next are not None before moving
- If slow == fast, there's a cycle

EDGE CASES:
- Empty list
- Single node with no cycle
- Single node with self-cycle
- Two nodes with cycle
- No cycle (linear list)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    # TODO: Implement your solution here
    pass

# Helper function to create linked list with cycle
def createLinkedListWithCycle(arr, pos):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    cycle_node = None
    
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
        if i == pos:
            cycle_node = curr
    
    if pos >= 0:
        curr.next = cycle_node
    
    return head

# Test your solution
if __name__ == "__main__":
    # Test case 1: Cycle exists
    head1 = createLinkedListWithCycle([3, 2, 0, -4], 1)
    print(f"Input: [3,2,0,-4] with cycle at position 1")
    print(f"Output: {hasCycle(head1)}")  # Expected: True
    
    # Test case 2: No cycle
    head2 = createLinkedListWithCycle([1, 2], -1)
    print(f"Input: [1,2] with no cycle")
    print(f"Output: {hasCycle(head2)}")  # Expected: False
    
    # Test case 3: Single node with cycle
    head3 = createLinkedListWithCycle([1], 0)
    print(f"Input: [1] with self-cycle")
    print(f"Output: {hasCycle(head3)}")  # Expected: True
