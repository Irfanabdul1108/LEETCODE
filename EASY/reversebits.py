# platform - leetcode
#link - https://leetcode.com/problems/reverse-bits/
# concept -  reverse the bits of an binary number

class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            bit=(n>>i)&1
            res=res|(bit<<(31-i))
        return res

