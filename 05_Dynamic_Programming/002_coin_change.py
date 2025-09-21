"""
LeetCode #322: Coin Change
Difficulty: Medium
Key Pattern: Unbounded Knapsack
Time: O(amount * coins), Space: O(amount)

PROBLEM:
You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money 
cannot be made up by any combination of the coins, return -1.

Example:
Input: coins = [1,3,4], amount = 6
Output: 2
Explanation: 6 = 3 + 3

HOW TO THINK:
1. This is an unbounded knapsack problem
2. For each amount, try all coins and take minimum
3. Use dynamic programming to avoid recalculating

THINKING STEPS:
1. Create dp array where dp[i] = minimum coins for amount i
2. Initialize dp[0] = 0, others = infinity
3. For each amount from 1 to target:
   - For each coin, if coin <= amount:
     - dp[amount] = min(dp[amount], dp[amount-coin] + 1)
4. Return dp[amount] if it's not infinity, else -1

HINTS:
- Use bottom-up dynamic programming
- dp[i] represents minimum coins needed for amount i
- For each amount, try all possible coins
- Take minimum of current value and (amount-coin) + 1

EDGE CASES:
- Amount = 0 (return 0)
- Impossible to make amount (return -1)
- Single coin type
- Large amount with small coins
"""

def coinChange(coins, amount):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    coins1 = [1, 3, 4]
    amount1 = 6
    print(f"Input: coins = {coins1}, amount = {amount1}")
    print(f"Output: {coinChange(coins1, amount1)}")  # Expected: 2
    
    # Test case 2
    coins2 = [2]
    amount2 = 3
    print(f"Input: coins = {coins2}, amount = {amount2}")
    print(f"Output: {coinChange(coins2, amount2)}")  # Expected: -1
    
    # Test case 3
    coins3 = [1]
    amount3 = 0
    print(f"Input: coins = {coins3}, amount = {amount3}")
    print(f"Output: {coinChange(coins3, amount3)}")  # Expected: 0
