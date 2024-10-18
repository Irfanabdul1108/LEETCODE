# platform - leetcode
#link - https://leetcode.com/problems/majority-element/description/
# concept - finding majority element in an array

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        for i,j in dict1.items():
            if j>(len(nums)//2):
                return i
            
        

