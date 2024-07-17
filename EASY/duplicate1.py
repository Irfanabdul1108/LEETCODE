# platform - leetcode
#link - https://leetcode.com/problems/contains-duplicate/
# concept -  contains duplicate or not

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        if len(nums)==len(nums1):
            return False
        return True 



