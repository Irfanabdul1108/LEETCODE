# platform - leetcode
#link - https://leetcode.com/problems/find-the-difference/
# concept - find the difference of two strings (s&t) that means find the extra character which is in the t string

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        for i,j in dict1.items():
            if j>(len(nums)//2):
                return i
            
        

