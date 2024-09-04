# platform - leetcode
#link - https://leetcode.com/problems/single-number/description/
# concept - find single number in an array

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans=ans^i
        return ans

