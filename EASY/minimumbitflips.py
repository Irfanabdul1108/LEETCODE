# platform - leetcode
#link - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# concept -  minimum bit flips to convert from start to goal (start and goal are integers)

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums=[]
        for i in range(0,n+1):
            m = bin(i)[2:].count('1')
            nums.append(m)
        return nums


