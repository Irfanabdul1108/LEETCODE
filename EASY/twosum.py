# platform - leetcode
#link - https://leetcode.com/problems/two-sum/
# concept - adding two numbers should give the target (less than o(n^2) time complexity)
 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,j in enumerate(nums):
            comp=target-j
            if comp in dict1:
                return [dict1[comp],i]
            dict1[j]=i
        
        