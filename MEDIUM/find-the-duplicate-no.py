# platform - leetcode
#link - https://leetcode.com/problems/find-the-duplicate-number/description/
# concept - finding the duplicate number

from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        list2=dict(Counter(nums))
        for i,j in list2.items():
            if j>=2:
                return i
    
        
        