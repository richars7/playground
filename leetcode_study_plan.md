# LeetCode Study Plan: Easy to Medium Problems
## Based on Interview Frequency

### Table of Contents
1. [Study Plan Overview](#study-plan-overview)
2. [Problem-Solving Framework](#problem-solving-framework)
3. [Week-by-Week Breakdown](#week-by-week-breakdown)
4. [Problem Categories & Solutions](#problem-categories--solutions)
5. [Advanced Strategies](#advanced-strategies)
6. [Practice Schedule](#practice-schedule)

---

## Study Plan Overview

**Duration**: 8 weeks  
**Daily Commitment**: 1-2 hours  
**Goal**: Master the most frequently asked LeetCode problems from easy to medium difficulty

### Why This Plan Works
- Focuses on **high-frequency interview questions**
- Builds foundational problem-solving skills
- Covers all major data structures and algorithms
- Includes practical hints and thinking patterns

---

## Problem-Solving Framework

### The 4-Step Approach
1. **Understand** - Read the problem carefully, identify inputs/outputs
2. **Plan** - Think about approach, time/space complexity
3. **Code** - Implement your solution
4. **Test** - Verify with examples and edge cases

### Key Thinking Patterns
- **Two Pointers**: For array/string problems with linear traversal
- **Sliding Window**: For substring/subarray problems
- **Hash Map**: For fast lookups and frequency counting
- **Stack/Queue**: For LIFO/FIFO operations
- **Recursion**: For tree/graph traversal and backtracking
- **Dynamic Programming**: For optimization problems with overlapping subproblems

---

## Week-by-Week Breakdown

### Week 1: Arrays & Strings (Foundation)
**Focus**: Basic array manipulation and string operations

#### Problems to Solve:
1. **Two Sum** (Easy) - *Most asked problem*
2. **Valid Anagram** (Easy)
3. **Longest Substring Without Repeating Characters** (Medium)
4. **Container With Most Water** (Medium)
5. **3Sum** (Medium)

#### Key Concepts:
- Hash maps for O(1) lookups
- Two-pointer technique
- Sliding window for substrings

#### Hints & Thinking:
- **Two Sum**: Use hash map to store complements
- **Valid Anagram**: Count character frequencies
- **Longest Substring**: Use sliding window with hash set
- **Container**: Two pointers from both ends
- **3Sum**: Sort array, fix one element, use two pointers

---

### Week 2: Linked Lists
**Focus**: Pointer manipulation and traversal

#### Problems to Solve:
1. **Reverse Linked List** (Easy)
2. **Linked List Cycle** (Easy)
3. **Merge Two Sorted Lists** (Easy)
4. **Remove Nth Node From End** (Medium)
5. **Copy List with Random Pointer** (Medium)

#### Key Concepts:
- Pointer manipulation
- Floyd's cycle detection algorithm
- Dummy nodes for edge cases

#### Hints & Thinking:
- **Reverse**: Use three pointers (prev, curr, next)
- **Cycle**: Use slow and fast pointers
- **Merge**: Compare values and link nodes
- **Remove Nth**: Use two pointers with n gap
- **Copy**: Use hash map for random pointer mapping

---

### Week 3: Stacks & Queues
**Focus**: LIFO and FIFO data structures

#### Problems to Solve:
1. **Valid Parentheses** (Easy)
2. **Min Stack** (Easy)
3. **Implement Queue using Stacks** (Easy)
4. **Daily Temperatures** (Medium)
5. **Largest Rectangle in Histogram** (Hard - but important)

#### Key Concepts:
- Stack for matching problems
- Monotonic stack for next greater/smaller elements
- Queue simulation with stacks

#### Hints & Thinking:
- **Valid Parentheses**: Use stack to match brackets
- **Min Stack**: Keep track of minimum at each level
- **Queue with Stacks**: Use two stacks (input/output)
- **Daily Temperatures**: Monotonic decreasing stack
- **Largest Rectangle**: Monotonic increasing stack

---

### Week 4: Trees & Binary Search
**Focus**: Tree traversal and binary search

#### Problems to Solve:
1. **Maximum Depth of Binary Tree** (Easy)
2. **Same Tree** (Easy)
3. **Invert Binary Tree** (Easy)
4. **Binary Search** (Easy)
5. **Search in Rotated Sorted Array** (Medium)

#### Key Concepts:
- Recursive tree traversal (DFS)
- Iterative traversal with stack
- Binary search variations

#### Hints & Thinking:
- **Max Depth**: Recursive: 1 + max(left, right)
- **Same Tree**: Compare values and recursively check children
- **Invert**: Swap left and right children recursively
- **Binary Search**: Keep track of left and right boundaries
- **Rotated Array**: Find pivot, then search in appropriate half

---

### Week 5: Dynamic Programming (Introduction)
**Focus**: Basic DP patterns

#### Problems to Solve:
1. **Climbing Stairs** (Easy)
2. **Best Time to Buy and Sell Stock** (Easy)
3. **House Robber** (Medium)
4. **Longest Common Subsequence** (Medium)
5. **Word Break** (Medium)

#### Key Concepts:
- Overlapping subproblems
- Optimal substructure
- Memoization vs tabulation

#### Hints & Thinking:
- **Climbing Stairs**: f(n) = f(n-1) + f(n-2)
- **Best Time**: Track minimum price and maximum profit
- **House Robber**: rob(i) = max(rob(i-1), rob(i-2) + nums[i])
- **LCS**: 2D DP table, if chars match: dp[i][j] = 1 + dp[i-1][j-1]
- **Word Break**: Check if substring exists in wordDict

---

### Week 6: Backtracking
**Focus**: Recursive exploration with pruning

#### Problems to Solve:
1. **Subsets** (Medium)
2. **Permutations** (Medium)
3. **Combination Sum** (Medium)
4. **Generate Parentheses** (Medium)
5. **N-Queens** (Hard - but important pattern)

#### Key Concepts:
- Decision tree exploration
- Backtracking with state restoration
- Pruning invalid paths

#### Hints & Thinking:
- **Subsets**: For each element, choose to include or exclude
- **Permutations**: Use visited array to track used elements
- **Combination Sum**: Sort array, use index to avoid duplicates
- **Generate Parentheses**: Track open and close counts
- **N-Queens**: Check diagonal and column conflicts

---

### Week 7: Graphs
**Focus**: Graph traversal algorithms

#### Problems to Solve:
1. **Number of Islands** (Medium)
2. **Clone Graph** (Medium)
3. **Course Schedule** (Medium)
4. **Word Ladder** (Hard - but important)
5. **Pacific Atlantic Water Flow** (Medium)

#### Key Concepts:
- DFS and BFS traversal
- Graph representation (adjacency list/matrix)
- Cycle detection
- Topological sorting

#### Hints & Thinking:
- **Number of Islands**: DFS to mark connected components
- **Clone Graph**: Use hash map to avoid cycles
- **Course Schedule**: Topological sort with cycle detection
- **Word Ladder**: BFS with word transformation
- **Pacific Atlantic**: DFS from ocean boundaries

---

### Week 8: Review & Advanced Patterns
**Focus**: Integration and optimization

#### Activities:
1. **Review challenging problems** from previous weeks
2. **Mock interviews** with time constraints
3. **Pattern recognition** exercises
4. **Optimization** of previous solutions

#### Advanced Patterns to Master:
- **Sliding Window**: Fixed and variable size
- **Two Pointers**: Opposite directions and same direction
- **Fast & Slow Pointers**: Cycle detection
- **Merge Intervals**: Sorting and merging
- **Tree BFS**: Level-order traversal
- **Subsets**: Bit manipulation approach

---

## Problem Categories & Solutions

### Arrays & Strings

#### Two Sum
```python
def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []
```
**Key Insight**: Use hash map to store complements for O(1) lookup

#### Longest Substring Without Repeating Characters
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```
**Key Insight**: Sliding window with hash set to track characters

### Linked Lists

#### Reverse Linked List
```python
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev
```
**Key Insight**: Use three pointers to reverse links

#### Linked List Cycle
```python
def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False
```
**Key Insight**: Floyd's cycle detection with slow and fast pointers

### Trees

#### Maximum Depth of Binary Tree
```python
def maxDepth(root):
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)
```
**Key Insight**: Recursive approach with base case

### Dynamic Programming

#### Climbing Stairs
```python
def climbStairs(n):
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1
```
**Key Insight**: Fibonacci sequence with space optimization

---

## Advanced Strategies

### Time Complexity Optimization
1. **Sorting**: O(n log n) - Use when you can trade time for space
2. **Hash Maps**: O(1) average lookup - Use for frequency counting
3. **Two Pointers**: O(n) - Use for sorted arrays or palindromes
4. **Sliding Window**: O(n) - Use for substring/subarray problems

### Space Complexity Optimization
1. **In-place algorithms**: Modify input array when possible
2. **Iterative over recursive**: Avoid call stack overhead
3. **Bit manipulation**: Use bits for boolean arrays
4. **Rolling variables**: Keep only necessary previous states

### Common Pitfalls to Avoid
1. **Off-by-one errors**: Be careful with array indices
2. **Integer overflow**: Use appropriate data types
3. **Edge cases**: Empty arrays, single elements, duplicates
4. **Infinite loops**: Always update loop variables
5. **Memory leaks**: Clean up temporary data structures

---

## Practice Schedule

### Daily Routine (1-2 hours)
- **30 minutes**: Review previous day's problems
- **60 minutes**: Solve new problems
- **30 minutes**: Read solutions and understand optimizations

### Weekly Goals
- **Monday-Wednesday**: Learn new concepts and solve problems
- **Thursday-Friday**: Practice variations and edge cases
- **Saturday**: Review week's problems and identify patterns
- **Sunday**: Mock interview or timed practice

### Progress Tracking
- Keep a log of solved problems
- Note time complexity and space complexity
- Record common mistakes and learnings
- Track improvement in problem-solving speed

### Resources
- **LeetCode**: Primary platform for practice
- **NeetCode**: Video explanations and curated lists
- **Blind 75**: Essential problems list
- **LeetCode Discuss**: Community solutions and insights

---

## Final Tips

1. **Consistency is key**: Practice daily, even if just 30 minutes
2. **Understand, don't memorize**: Focus on patterns and principles
3. **Time yourself**: Practice under interview conditions
4. **Explain your approach**: Verbalize your thinking process
5. **Learn from mistakes**: Review failed attempts and understand why
6. **Stay updated**: Follow new problem patterns and company-specific questions

Remember: The goal is not just to solve problems, but to develop strong problem-solving intuition that will serve you in any technical interview!

---

*Good luck with your LeetCode journey! 🚀*
