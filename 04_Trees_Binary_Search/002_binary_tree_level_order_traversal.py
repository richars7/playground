"""
LeetCode #102: Binary Tree Level Order Traversal
Difficulty: Medium
Key Pattern: BFS with Queue
Time: O(n), Space: O(w) where w is max width

PROBLEM:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

HOW TO THINK:
1. Use BFS (Breadth-First Search) with a queue
2. Process nodes level by level
3. For each level, collect all nodes and their children

THINKING STEPS:
1. Use a queue to store nodes to process
2. While queue is not empty:
   - Get current level size
   - Process all nodes in current level
   - Add their children to queue for next level
3. Add current level to result

HINTS:
- Use a queue (deque) for BFS
- Track level size to process level by level
- Add children to queue for next iteration
- Don't forget to handle None children

EDGE CASES:
- Empty tree
- Single node tree
- Skewed tree
- Balanced tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    # TODO: Implement your solution here
    pass

# Helper function to create binary tree from array
def createBinaryTree(arr):
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test your solution
if __name__ == "__main__":
    # Test case 1
    root1 = createBinaryTree([3, 9, 20, None, None, 15, 7])
    print(f"Input: [3,9,20,null,null,15,7]")
    print(f"Output: {levelOrder(root1)}")  # Expected: [[3],[9,20],[15,7]]
    
    # Test case 2
    root2 = createBinaryTree([1])
    print(f"Input: [1]")
    print(f"Output: {levelOrder(root2)}")  # Expected: [[1]]
    
    # Test case 3
    root3 = createBinaryTree([])
    print(f"Input: []")
    print(f"Output: {levelOrder(root3)}")  # Expected: []
