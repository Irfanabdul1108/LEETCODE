# platform - leetcode
#link - https://leetcode.com/problems/missing-number/
# concept - missing number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p=len(nums)
        if p in nums:
            return ((p*(p+1))//2)-sum(nums)
        else:
            return p
