"""
LeetCode #21: Merge Two Sorted Lists
Difficulty: Easy
Key Pattern: Two Pointers + Dummy Node
Time: O(n+m), Space: O(1)

PROBLEM:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together 
the nodes of the first two lists.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

HOW TO THINK:
1. Compare values of current nodes from both lists
2. Add the smaller value to result list
3. Move the pointer of the list that contributed the smaller value
4. Use a dummy node to simplify edge cases

THINKING STEPS:
1. Create a dummy node to start the result list
2. Use a current pointer to build the result
3. While both lists have nodes:
   - Compare values
   - Add smaller value to result
   - Move appropriate pointer
4. Add remaining nodes from either list
5. Return dummy.next

HINTS:
- Use a dummy node to avoid handling empty result list
- Compare values and add smaller one to result
- Don't forget to add remaining nodes after one list is exhausted
- The dummy node's next will be the actual head

EDGE CASES:
- One or both lists are empty
- One list is much longer than the other
- All values in one list are smaller than the other
- Duplicate values
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
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
    list1 = createLinkedList([1, 2, 4])
    list2 = createLinkedList([1, 3, 4])
    print(f"Input: list1 = {linkedListToArray(list1)}, list2 = {linkedListToArray(list2)}")
    merged = mergeTwoLists(list1, list2)
    print(f"Output: {linkedListToArray(merged)}")  # Expected: [1,1,2,3,4,4]
    
    # Test case 2
    list3 = createLinkedList([])
    list4 = createLinkedList([])
    print(f"Input: list1 = {linkedListToArray(list3)}, list2 = {linkedListToArray(list4)}")
    merged2 = mergeTwoLists(list3, list4)
    print(f"Output: {linkedListToArray(merged2)}")  # Expected: []
    
    # Test case 3
    list5 = createLinkedList([])
    list6 = createLinkedList([0])
    print(f"Input: list1 = {linkedListToArray(list5)}, list2 = {linkedListToArray(list6)}")
    merged3 = mergeTwoLists(list5, list6)
    print(f"Output: {linkedListToArray(merged3)}")  # Expected: [0]
