"""
LeetCode #134: Gas Station
Difficulty: Medium
Key Pattern: Greedy Algorithm
Time: O(n), Space: O(1)

PROBLEM:
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel 
around the circuit once in the clockwise direction, otherwise return -1.

Example:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your tank = 5 - 5 = 0
Since your tank >= 0 at all times, return 3.

HOW TO THINK:
1. If total gas < total cost, impossible to complete circuit
2. If we can't reach station j from station i, then we can't reach j from any station between i and j
3. Start from station 0, if we can't reach station i, start from i+1

THINKING STEPS:
1. Check if total gas >= total cost
2. Start from station 0, track current tank
3. If tank becomes negative, reset start to next station
4. Return start index if we complete the circuit

HINTS:
- Use greedy approach: if we can't reach station j from i, start from j+1
- Track total gas and total cost
- If total gas < total cost, return -1
- Reset start position when tank becomes negative

EDGE CASES:
- Single station
- All stations have enough gas
- No valid starting station
- Circuit can be completed from any station
"""

def canCompleteCircuit(gas, cost):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    gas1 = [1,2,3,4,5]
    cost1 = [3,4,5,1,2]
    print(f"Input: gas = {gas1}, cost = {cost1}")
    print(f"Output: {canCompleteCircuit(gas1, cost1)}")  # Expected: 3
    
    # Test case 2
    gas2 = [2,3,4]
    cost2 = [3,4,3]
    print(f"Input: gas = {gas2}, cost = {cost2}")
    print(f"Output: {canCompleteCircuit(gas2, cost2)}")  # Expected: -1
    
    # Test case 3
    gas3 = [5,1,2,3,4]
    cost3 = [4,4,1,5,1]
    print(f"Input: gas = {gas3}, cost = {cost3}")
    print(f"Output: {canCompleteCircuit(gas3, cost3)}")  # Expected: 4
