"""
LeetCode #56: Merge Intervals
Difficulty: Medium
Key Pattern: Sorting + Greedy
Time: O(n log n), Space: O(1)

PROBLEM:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

HOW TO THINK:
1. Sort intervals by start time
2. For each interval, check if it overlaps with the previous merged interval
3. If it overlaps, merge them; if not, add it as a new interval

THINKING STEPS:
1. Sort intervals by start time
2. Initialize result with first interval
3. For each subsequent interval:
   - If it overlaps with last interval in result, merge them
   - If not, add it to result
4. Two intervals overlap if start of current <= end of previous

HINTS:
- Sort intervals by start time first
- Use greedy approach: merge overlapping intervals
- Two intervals [a,b] and [c,d] overlap if c <= b
- When merging, take min of starts and max of ends

EDGE CASES:
- Empty intervals array
- Single interval
- No overlapping intervals
- All intervals overlap
- Intervals with same start/end times
"""

def merge(intervals):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(f"Input: {intervals1}")
    print(f"Output: {merge(intervals1)}")  # Expected: [[1,6],[8,10],[15,18]]
    
    # Test case 2
    intervals2 = [[1,4],[4,5]]
    print(f"Input: {intervals2}")
    print(f"Output: {merge(intervals2)}")  # Expected: [[1,5]]
    
    # Test case 3
    intervals3 = [[1,4],[0,4]]
    print(f"Input: {intervals3}")
    print(f"Output: {merge(intervals3)}")  # Expected: [[0,4]]
