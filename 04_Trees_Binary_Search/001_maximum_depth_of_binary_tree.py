"""
LeetCode #104: Maximum Depth of Binary Tree
Difficulty: Easy
Key Pattern: Recursive DFS
Time: O(n), Space: O(h) where h is height

PROBLEM:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

HOW TO THINK:
1. The depth of a tree is 1 + max(depth of left subtree, depth of right subtree)
2. Base case: if node is None, depth is 0
3. Recursive case: return 1 + max of left and right depths

THINKING STEPS:
1. If root is None, return 0 (base case)
2. Recursively find depth of left subtree
3. Recursively find depth of right subtree
4. Return 1 + max(left_depth, right_depth)

HINTS:
- Use recursion to solve this
- Base case: empty tree has depth 0
- Recursive case: depth = 1 + max(left_depth, right_depth)
- This is a classic tree traversal problem

EDGE CASES:
- Empty tree (None)
- Single node tree
- Skewed tree (all nodes on one side)
- Balanced tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
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
    print(f"Output: {maxDepth(root1)}")  # Expected: 3
    
    # Test case 2
    root2 = createBinaryTree([1, None, 2])
    print(f"Input: [1,null,2]")
    print(f"Output: {maxDepth(root2)}")  # Expected: 2
    
    # Test case 3
    root3 = createBinaryTree([])
    print(f"Input: []")
    print(f"Output: {maxDepth(root3)}")  # Expected: 0
