# platform - leetcode
#link - https://leetcode.com/problems/counting-bits/
# concept -  counting bits in an number

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums=[]
        for i in range(0,n+1):
            m = bin(i)[2:].count('1')
            nums.append(m)
        return nums


