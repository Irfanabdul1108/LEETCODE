# platform - leetcode
#link - https://leetcode.com/problems/number-of-1-bits/description/
# concept - caluclating no of 1 bits using bit manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        m=bin(n)[2:]
        return m.count('1')
        