"""
LeetCode #200: Number of Islands
Difficulty: Medium
Key Pattern: DFS/BFS on Grid
Time: O(m*n), Space: O(m*n)

PROBLEM:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

HOW TO THINK:
1. This is a connected components problem on a grid
2. Use DFS or BFS to explore each island
3. Mark visited cells to avoid counting the same island multiple times
4. Count the number of times we start a new DFS/BFS

THINKING STEPS:
1. Iterate through each cell in the grid
2. If cell is '1' and not visited, start DFS/BFS
3. During DFS/BFS, mark all connected '1's as visited
4. Increment island count
5. Return total count

HINTS:
- Use DFS or BFS to explore connected components
- Mark visited cells (change '1' to '0' or use visited array)
- Check all 4 directions: up, down, left, right
- Count the number of times you start a new exploration

EDGE CASES:
- Empty grid
- Grid with no islands (all '0's)
- Grid with all islands (all '1's)
- Single cell grid
- Islands touching the edges
"""

def numIslands(grid):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Input: {grid1}")
    print(f"Output: {numIslands(grid1)}")  # Expected: 1
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Input: {grid2}")
    print(f"Output: {numIslands(grid2)}")  # Expected: 3
    
    # Test case 3
    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(f"Input: {grid3}")
    print(f"Output: {numIslands(grid3)}")  # Expected: 1
