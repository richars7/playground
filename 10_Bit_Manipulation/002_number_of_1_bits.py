"""
LeetCode #191: Number of 1 Bits
Difficulty: Easy
Key Pattern: Bit Manipulation
Time: O(1), Space: O(1)

PROBLEM:
Write a function that takes an unsigned integer and returns the number of '1' bits it has 
(also known as the Hamming weight).

Example:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

HOW TO THINK:
1. Check each bit of the number
2. Count how many bits are set to 1
3. Use bit manipulation to check each bit

THINKING STEPS:
1. Initialize count = 0
2. While n > 0:
   - If n & 1 == 1, increment count
   - Right shift n by 1
3. Return count

HINTS:
- Use bitwise AND with 1 to check least significant bit
- Right shift to move to next bit
- Alternative: use n & (n-1) to remove rightmost 1 bit
- Continue until n becomes 0

EDGE CASES:
- n = 0 (no 1 bits)
- n = 1 (one 1 bit)
- All bits are 1
- Only one bit is 1
"""

def hammingWeight(n):
    # TODO: Implement your solution here
    pass

# Test your solution
if __name__ == "__main__":
    # Test case 1
    n1 = 11  # Binary: 1011
    print(f"Input: n = {n1} (binary: {bin(n1)})")
    print(f"Output: {hammingWeight(n1)}")  # Expected: 3
    
    # Test case 2
    n2 = 128  # Binary: 10000000
    print(f"Input: n = {n2} (binary: {bin(n2)})")
    print(f"Output: {hammingWeight(n2)}")  # Expected: 1
    
    # Test case 3
    n3 = 4294967293  # Binary: 11111111111111111111111111111101
    print(f"Input: n = {n3} (binary: {bin(n3)})")
    print(f"Output: {hammingWeight(n3)}")  # Expected: 31
